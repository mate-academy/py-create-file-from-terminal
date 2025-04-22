import pytest

from app.create_file import parse_sys_argv


@pytest.mark.parametrize(
    "command, result",
    [
        (['app/create_file.py', '-d', 'dir1', 'dir2', '-f', 'file.txt'], {"path": "dir1\dir2", "name_file": "file.txt"}),
        (['app/create_file.py', '-f', 'file.txt', '-d', 'dir1', 'dir2'], {"path": "dir1\dir2", "name_file": "file.txt"}),
        (['app/create_file.py', '-f', 'file.txt'], {"path": None, "name_file": "file.txt"}),
        (['app/create_file.py', '-d', 'dir1', 'dir2'], {"path": "dir1\dir2", "name_file": None}),
    ],
    ids=[
        "dir_then_file",
        "file_then_dir",
        "only_file_provided",
        "only_dir_provided",
    ]
)
def test_func_parse_sys_argv(command: list, result: dict) -> None:
    assert parse_sys_argv(command) == result