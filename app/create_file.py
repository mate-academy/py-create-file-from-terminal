import os
import argparse
from argparse import Namespace
from datetime import datetime


def getting_the_file_and_directories_from_terminal() -> Namespace:
    arguments = argparse.ArgumentParser(
        description="Input the path to create the file.\n"
                    "Use flags `-d` and `-f` to specify the catalogues"
                    "and file name to create.")

    arguments.add_argument(
        "-d", nargs="*", type=str, help="The queue of directories to create")
    arguments.add_argument(
        "-f", type=str, help="The name of file and type"
    )

    return arguments.parse_args()


def get_timestamp_of_current_date_and_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def getting_current_dir_and_check_file_existence() -> None:
    args = getting_the_file_and_directories_from_terminal()
    file_name = args.f
    dirs = args.d or []

    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)
        file_name = os.path.join(*dirs, file_name)
    else:
        file_name = os.path.join(os.getcwd(), file_name)

    mode = "a+" if os.path.exists(file_name) else "w"
    content = get_timestamp_of_current_date_and_time() + "\n"
    content = compile_content(content)
    if mode == "a+":
        content = "\n" + content
    file_creation_or_modification(file_name, mode, content)


def file_creation_or_modification(
        file_path: str,
        mode: str,
        content: str
) -> None:
    with open(file_path, mode) as file:
        file.write(content)


def compile_content(content: str) -> str:
    while True:
        c_line = input("Enter content line: ")
        if c_line != "stop":
            content += str(content.count("\n")) + " " + c_line + "\n"
        else:
            break

    return content


if __name__ == "__main__":
    getting_current_dir_and_check_file_existence()
