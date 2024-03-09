import os
import sys
import unittest
from datetime import datetime
from unittest.mock import patch, mock_open

from app.create_file import parse_arguments, create_file

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))


class TestParseArguments(unittest.TestCase):
    def test_parse_arguments(self):
        args = ["-d", "dir1", "dir2", "-f", "file.txt"]
        expected = {'-d': ['dir1', 'dir2'], '-f': 'file.txt'}
        self.assertEqual(parse_arguments(args), expected)


class TestMain(unittest.TestCase):
    @patch("builtins.input", side_effect=["Line1 content", "Line2 content", "stop"])
    @patch("builtins.open", new_callable=mock_open, read_data="data")
    @patch("os.makedirs")
    def test_file_creation_with_content(self, mock_makedirs, mock_file,
                                        mock_input):
        current_datetime_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        args = ["-f", "file.txt"]
        flags = parse_arguments(args)
        create_file("", flags["-f"], ["Line1 content", "Line2 content"])

        mock_file.assert_called_with("file.txt", "a")
        handle = mock_file.return_value
        handle.write.assert_any_call(f"{current_datetime_str}\n")
        handle.write.assert_any_call("1 Line1 content\n")
        handle.write.assert_any_call("2 Line2 content\n")


class TestDirectoryCreation(unittest.TestCase):
    @patch("builtins.input", side_effect=["stop"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_directory_creation(self, mock_makedirs, mock_file, mock_input):
        args = ["-d", "dir1", "-f", "file.txt"]
        flags = parse_arguments(args)
        create_file(flags["-d"][0], flags["-f"], [])

        mock_makedirs.assert_called_with("dir1", exist_ok=True)

        mock_file.assert_called_with(os.path.join("dir1", "file.txt"), "a")
