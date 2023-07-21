import os

import sys

from datetime import datetime

from typing import List


def create_file() -> None:
    list_of_arguments = sys.argv[1:]

    def create_directory(args: List[str], file_exists: bool = False) -> str:
        index_d = list_of_arguments.index("-d") + 1
        index_f = list_of_arguments.index("-f") if file_exists else None
        list_of_directories = list_of_arguments[index_d: index_f]
        path_for_new_dirs = os.path.join(*list_of_directories)
        os.makedirs(path_for_new_dirs, exist_ok=True)
        if index_f is not None:
            return os.path.abspath(path_for_new_dirs)

    def create_new_file(args: List[str], path: str = "") -> None:
        index_f = args.index("-f") + 1
        file_name = list_of_arguments[index_f]
        path_for_file = (os.path.join(path, file_name)
                         if path != "" else file_name)
        write_content_to_file(path_for_file)

    def write_content_to_file(path_for_file: str) -> None:
        with open(path_for_file, "a") as new_file:
            content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line_count = 0
            new_file.write(f"{content}\n")
        while True:
            call_to_action = input("Enter content line: ")
            line_count += 1
            if call_to_action == "stop":
                with open(path_for_file, "a") as file:
                    file.write("\n")
                break
            with open(path_for_file, "a") as file:
                file.write(f"{line_count} {call_to_action}\n")
    if "-d" in list_of_arguments and "-f" not in list_of_arguments:
        create_directory(list_of_arguments, False)
    if "-f" in list_of_arguments and "-d" not in list_of_arguments:
        create_new_file(list_of_arguments)
    if "-d" in list_of_arguments and "-f" in list_of_arguments:
        path_for_file = create_directory(list_of_arguments, True)
        create_new_file(list_of_arguments, path_for_file)


if __name__ == "__main__":
    create_file()
