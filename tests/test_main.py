import os
import shutil
from unittest.mock import patch
from app.create_file import create_app


def test_create_file_simple():
    folder = "my_folder"
    filename = "hello.txt"
    path_to_file = os.path.join(folder, filename)

    if os.path.exists(folder):
        shutil.rmtree(folder)

    mock_args = ['create_file.py', '-d', folder, '-f', filename]

    mock_input = ["Привіт", "stop"]

    with patch('sys.argv', mock_args), patch('builtins.input', side_effect=mock_input):
        create_app()

    assert os.path.exists(path_to_file) == True

    with open(path_to_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "1 Привіт" in content

    shutil.rmtree(folder)
