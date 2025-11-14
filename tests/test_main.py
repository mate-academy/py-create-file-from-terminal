import unittest
import os
import shutil
import sys
from unittest import mock

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(project_root, 'app'))

import app.create_file as create_file

test_dir = "temp_test_data"
mock_time_value = "2025-01-01 12:00:00"


class TestCreateFileLogic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
        os.makedirs(test_dir)
        os.chdir(test_dir)

    @classmethod
    def tearDownClass(cls):
        os.chdir("..")
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)

    def read_file_content(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    def test_01_parse_only_f_flag(self):
        args = ["script_name", create_file.file_flag, "my_file.txt"]
        dir_parts, file_name = create_file.parse_args(args)
        self.assertEqual(dir_parts, [])
        self.assertEqual(file_name, "my_file.txt")

    def test_02_parse_both_flags(self):
        args = ["script_name", create_file.dir_flag, "path1", "path2",
                create_file.file_flag, "final.log"]
        dir_parts, file_name = create_file.parse_args(args)
        self.assertEqual(dir_parts, ["path1", "path2"])
        self.assertEqual(file_name, "final.log")

    @mock.patch("app.create_file.get_timestamp",
                return_value=mock_time_value)
    def test_03_format_new_block(self, mock_time):
        input_lines = ["Line one", "Line two"]
        expected = f"\n{mock_time_value}\n1 Line one\n2 Line two\n"
        result = create_file.format_new_block(input_lines)
        self.assertEqual(result, expected)

    @mock.patch("builtins.input", side_effect=["Content A", "stop"])
    @mock.patch("app.create_file.get_timestamp",
                return_value=mock_time_value)
    def test_04_main_create_simple_file(self, mock_time, mock_input):
        file_name = "test_simple.txt"
        create_file.sys.argv = ["create_file.py", create_file.file_flag,
                                file_name]
        create_file.main()

        expected_content = f"\n{mock_time_value}\n1 Content A\n"
        self.assertTrue(os.path.exists(file_name))
        self.assertEqual(self.read_file_content(file_name), expected_content)

    @mock.patch("builtins.input",
                side_effect=["Initial content", "stop",
                             "New line B", "stop"])
    @mock.patch("app.create_file.get_timestamp",
                side_effect=["2025-01-01 12:00:00",
                             "2025-01-01 12:05:00"])
    def test_05_main_append_content(self, mock_time, mock_input):
        file_name = "test_append.txt"
        create_file.sys.argv = ["create_file.py", create_file.file_flag,
                                file_name]
        create_file.main()
        create_file.sys.argv = ["create_file.py", create_file.file_flag,
                                file_name]
        create_file.main()
        full_content = self.read_file_content(file_name)
        expected_part_1 = "\n2025-01-01 12:00:00\n1 Initial content\n"
        expected_part_2 = "\n2025-01-01 12:05:00\n1 New line B\n"

        self.assertIn(expected_part_1, full_content)
        self.assertIn(expected_part_2, full_content)

    @mock.patch("builtins.input", side_effect=["Content in dir", "stop"])
    @mock.patch("app.create_file.get_timestamp",
                return_value=mock_time_value)
    def test_06_main_create_dir_and_file(self, mock_time, mock_input):
        dir_path_expected = os.path.join("dir1", "dir2")
        file_name = "deep_file.log"
        full_path = os.path.join(dir_path_expected, file_name)

        create_file.sys.argv = ["create_file.py", create_file.dir_flag,
                                "dir1", "dir2", create_file.file_flag,
                                file_name]
        create_file.main()

        expected_content = f"\n{mock_time_value}\n1 Content in dir\n"

        self.assertTrue(os.path.exists(dir_path_expected))
        self.assertTrue(os.path.exists(full_path))
        self.assertEqual(self.read_file_content(full_path),
                         expected_content)


if __name__ == "__main__":
    unittest.main()