import os
import sys
from datetime import datetime


def add_new_content_line(path_to_file: str) -> None:
    with open(path_to_file, "a") as created_file:
        created_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while (added_line := input("Enter content line: ")) != "stop":
            created_file.write(f"{added_line}\n")
        created_file.write("\n")


def create_path_to_folders(path_data: list[str]) -> str:
    input_list = []
    for command in path_data[1:]:
        if "-f" not in command and "-d" not in command and "." not in command:
            input_list.append(command)
    return os.path.join(*input_list)


def create_path_to_file(path_data: list[str]) -> str:
    return os.path.join(path_data[path_data.index("-f") + 1])


def create_only_file(input_data: list[str]) -> None:
    add_new_content_line(create_path_to_file(input_data))


def create_only_folders(input_data: list[str]) -> None:
    os.makedirs(create_path_to_folders(input_data), exist_ok=True)


def create_folders_and_file(input_data: list[str]) -> None:
    create_only_folders(input_data)
    add_new_content_line(
        f"{create_path_to_folders(input_data)}"
        f"/{create_path_to_file(input_data)}"
    )


if __name__ == "__main__":
    if "-f" in sys.argv and "-d" not in sys.argv:
        create_only_file(sys.argv)
    if "-d" in sys.argv and "-f" not in sys.argv:
        create_only_folders(sys.argv)
    if "-d" in sys.argv and "-f" in sys.argv:
        create_folders_and_file(sys.argv)
