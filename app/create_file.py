import os

import sys

from datetime import datetime


def create_file() -> None:
    list_of_arguments = sys.argv[1:]

    def create_directory(args: list, file_exists: bool = False) -> str:
        index_d = list_of_arguments.index("-d") + 1
        if file_exists:
            index_f = list_of_arguments.index("-f")
        else:
            index_f = None

        list_of_directories = list_of_arguments[index_d: index_f]

        path_for_new_dirs = os.path.join(*list_of_directories)

        os.makedirs(path_for_new_dirs, exist_ok=True)

        if index_f is not None:
            return f"Path for new directories: {path_for_new_dirs}"

    def create_new_file(args: list, path: str = "") -> None:
        index_f = args.index("-f") + 1
        file_name = list_of_arguments[index_f]
        path_for_file = f"{path}/{file_name}" if path != "" else file_name

        with open(path_for_file, "w") as new_file:
            content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_file.write(f"{content}\n")

        while True:
            call_to_action = input("Enter content line: ")

            if call_to_action == "stop":
                break

            with open(path_for_file, "a") as file:
                file.write(f"{call_to_action}\n")

    if "-d" in list_of_arguments and "-f" not in list_of_arguments:
        create_directory(list_of_arguments, False)

    if "-f" in list_of_arguments and "-d" not in list_of_arguments:
        create_new_file(list_of_arguments)

    if "-d" in list_of_arguments and "-f" in list_of_arguments:
        path_for_file = create_directory(list_of_arguments, True)
        create_new_file(list_of_arguments, path_for_file)


if __name__ == "__main__":
    create_file()
