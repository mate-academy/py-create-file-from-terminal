import io
import shutil
from app.create_file import get_path, create_file
import os
import pytest
from unittest import mock


class TestClass:

    @classmethod
    def run_create_file_with_args_and_handle_empty_input(cls, args: str) -> None:
        return cls.run_create_file_with_args_and_handle_input(args, [])

    @classmethod
    def run_create_file_with_args_and_handle_input(cls, args: str, file_contents: list[str]) -> None:
        create_file(args)
        file_contents.append("stop")
        with mock.patch("builtins.input") as mock_input:
            for line in file_contents:            
                mock_input.return_value = line
                input()


    @classmethod
    def delete_file(cls, file_path: str) -> None:
        if os.path.isfile(file_path):
            os.remove(file_path)

    @classmethod
    def delete_directory(cls, folder: str) -> None:
        print(f"Deleting {folder}")
        if os.path.exists(folder):
            shutil.rmtree(folder)
        print(f"folder deleted: {not os.path.exists(folder)}")

    def test_file_not_created_when_f_arg_not_passed(self) -> None:
        folders = "nofiledir1 dir2 dir3"
        TestClass.delete_directory(folders)
        TestClass.run_create_file_with_args_and_handle_empty_input(f"-d {folders}")
        assert len(os.listdir(get_path(folders.split(" ")))) == 0

    def test_file_created_in_current_dir_when_d_arg_not_passed(self) -> None:
        TestClass.run_create_file_with_args_and_handle_empty_input("-f file.txt")
        assert os.path.isfile("file.txt")

    @pytest.mark.parametrize(
        "folders, filename",
        [
            ("dir1 dir2 dir3", "file1.txt"),
            ("dir2 dir3", "file2.txt"),
        ]
    )
    def test_file_created_in_right_directory(
            self,
            folders: str,
            filename: str
    ) -> None:
        dir_path = get_path(folders.split(" "))
        TestClass.delete_directory(dir_path)
        args = f"-d {folders} -f {filename}"
        TestClass.run_create_file_with_args_and_handle_empty_input(args)

        result = os.path.isfile(os.path.join(dir_path, filename))
        print(result)
        assert result

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown")
        TestClass.delete_directory("dir1")
        TestClass.delete_directory("dir2")
        TestClass.delete_directory("nofiledir1")
        TestClass.delete_file("file.txt")
