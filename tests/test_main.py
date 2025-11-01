import unittest
import os
import sys

from unittest.mock import patch, mock_open

from app.create_file import create_file


class TestCreateFileAndDirs(unittest.TestCase):
    """Tests file creation with nested directories and writing content."""

    @patch("builtins.input", side_effect=["First line", "Second line", "stop"])
    @patch("os.makedirs")
    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_create_file_creates_new_file(self, mock_file, mock_exists, mock_makedirs, mock_input):
        test_args = ["script_name", "-d", "test_dir", "test_dir2", "-f", "test_file.txt"]
        with patch.object(sys, "argv", test_args):
            create_file()

        # Check directory creation
        mock_makedirs.assert_called_once_with(os.path.join("test_dir", "test_dir2"), exist_ok=True)

        # Check file write
        mock_file.assert_called_once_with(os.path.join("test_dir", "test_dir2", "test_file.txt"), "a", encoding="utf-8")
        handle = mock_file()
        written_lines = [call.args[0].strip() for call in handle.write.call_args_list]
        self.assertTrue(any("1 First line" in line for line in written_lines))
        self.assertTrue(any("2 Second line" in line for line in written_lines))


class TestCreateDirs(unittest.TestCase):
    """Tests directory creation logic without writing content."""

    @patch("builtins.input", side_effect=["stop"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("os.path.exists", return_value=False)
    def test_create_file_creates_dirs(self, mock_exists, mock_makedirs, mock_file, mock_input):
        test_args = ["script_name", "-d", "test_dir", "-f", "test_file.txt"]
        with patch.object(sys, "argv", test_args):
            create_file()

        mock_makedirs.assert_called_once_with(os.path.join("test_dir"), exist_ok=True)


class TestCreateOnlyFile(unittest.TestCase):
    """Tests creating and writing to a file without directory arguments."""

    @patch("builtins.input", side_effect=["First line", "Second line", "stop"])
    @patch("os.makedirs")
    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_create_file_creates_new_file(self, mock_file, mock_exists, mock_makedirs, mock_input):
        test_args = ["script_name", "-f", "test_file.txt"]
        with patch.object(sys, "argv", test_args):
            create_file()


        # Check file write
        mock_file.assert_called_once_with(os.path.join("test_file.txt"), "a", encoding="utf-8")
        handle = mock_file()
        written_lines = [call.args[0].strip() for call in handle.write.call_args_list]
        self.assertTrue(any("1 First line" in line for line in written_lines))
        self.assertTrue(any("2 Second line" in line for line in written_lines))


if __name__ == "__main__":
    unittest.main()
