import unittest
from unittest import mock
from unittest.mock import patch
from app.create_file import create_folder, create_file, scan_args

class TestMain(unittest.TestCase):

    def test_scan_args(self) -> None:
        with patch("app.create_file.sys.argv",
                    ["create_file.py", "-d",
                    "test_folder"]) as mock_argv:
            d_args, f_args = scan_args()
            self.assertEqual(d_args, ["test_folder"])
            self.assertEqual(f_args, [])

        with patch("app.create_file.sys.argv",
                    ["create_file.py", "-d",
                    "test_folder", "-f",
                    "test_file"]) as mock_argv:
            d_args, f_args = scan_args()
            self.assertEqual(d_args, ["test_folder"])
            self.assertEqual(f_args, ["test_file"])
    
   