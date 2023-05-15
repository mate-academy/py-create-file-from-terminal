import sys
import os
from datetime import datetime


def content_for_new_file() -> list:
    content = []
    while True:
        line = input()
        if line == "stop":
            break
        content.append(line + "\n")
    return content


def write_content_in_new_file(
        file_name: str,
        mode: str,
        content: list
) -> None:
    with open(file_name, mode) as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.writelines(content)


def create_file() -> None:
    command_line = sys.argv
    if command_line[1] == "-f":
        content = content_for_new_file()
        write_content_in_new_file(command_line[-1], "w", content)
    elif command_line[1] == "-d":
        os.makedirs(os.path.join(*command_line[2::]))
    else:
        os.makedirs(os.path.join(*command_line[2:-1]))
        os.chdir(os.path.join(*command_line[2:-1]))
        content = content_for_new_file()
        write_content_in_new_file(command_line[-1], "w", content)


if __name__ == "__main__":
    create_file()
