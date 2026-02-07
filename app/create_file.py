import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file_in, open(file_path, "r") as file_out:
        if file_out.readlines():
            file_in.write("\n\n")
        file_in.write(f'{datetime.now().strftime("%y-%m-%d %H:%M:%S")}\n')
        line_number = 1
        content = []
        while True:
            line_content = input("Enter content line: ")
            if line_content.lower() == "stop":
                break
            content.append(f"{line_number} {line_content}")
            line_number += 1
        ready_content = "\n".join(content)
        file_in.write(ready_content)


def create_directory(directory_list: list) -> None:
    dir_path = os.path.join(*directory_list)
    os.makedirs(dir_path, exist_ok=True)


def main() -> None:
    args = sys.argv[1:]
    dir_list = []
    file_name = ""
    if "-d" in args:
        for arg in args[1:]:
            if arg == "-f":
                break
            dir_list.append(arg)
    if "-f" in args:
        file_name = args[-1]

    if dir_list:
        create_directory(dir_list)
        if file_name:
            file_path = os.path.join(*dir_list, file_name)
            create_file(file_path)
    elif file_name:
        create_file(file_name)


if __name__ == "__main__":
    main()
