import pytest
import os


from app.create_file import create_file_or_dir


@pytest.mark.parametrize(
    "command",
    [
        pytest.param(
            ['.\\app\\create-file.py', '-d', 'dir1', 'dir2', '-f', 'file.txt'],
            id="Test"
        ),
    ]
)
def test_create_file_or_dict(self, command: list) -> None:
    assert os.path.exists(create_file_or_dir(command))

