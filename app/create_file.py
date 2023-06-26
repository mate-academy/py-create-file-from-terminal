import os
import sys

from datetime import datetime


def create_directory(command: list[str]) -> str:
    path = ""
    if "-d" in command:
        d_index = command.index("-d")
        if "-f" in command:
            f_index = command.index("-f")
            if f_index > d_index:
                path = os.path.join(*(command[f_index + 1:d_index]))
            else:
                path = os.path.join(*(command[d_index + 1::]))
        else:
            path = os.path.join(*(command[d_index + 1::]))
        if path:
            os.makedirs(path, exist_ok=True)
    return path


def create_content() -> list[str]:
    content = []
    while True:
        content_line = input("Enter content line:")
        if content_line == "stop":
            break
        content.append(content_line + "\n")
        print(content)
    return content


def write_into_file(path: str, file_name: str, content: list[str]) -> None:
    with open(os.path.join(path, file_name), "a") as new_file:
        new_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for line in content:
            new_file.write(line)


def create_file_inside_directory() -> None:
    cmd_list = sys.argv
    path = create_directory(cmd_list)
    if "-f" in cmd_list:
        file_name = cmd_list[cmd_list.index("-f") + 1]
        content = create_content()
        write_into_file(path, file_name, content)
    print("path: ", path)


if __name__ == "__main__":
    create_file_inside_directory()
