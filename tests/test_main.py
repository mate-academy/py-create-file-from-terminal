import os.path

from app.create_file import create_file_and_dir


def test_directory_should_created() -> None:
    create_file_and_dir(["app\create_file.py", "-d", "dir1", "dir2"])
    assert (
        os.path.exists(
            "C:\\Users\\Skrev\\PycharmProjects\\py-create-file-from-terminal\\tests\\dir1\\dir2"
        )
        == True
    )
    os.removedirs(
        "C:\\Users\\Skrev\\PycharmProjects\\py-create-file-from-terminal\\tests\\dir1\\dir2"
    )
