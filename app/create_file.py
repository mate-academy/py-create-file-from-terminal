import sys
import os
from datetime import datetime


def create_content_for_new_file() -> list:
    content = []
    while True:
        line = input()
        if line == "stop":
            break
        content.append(line + "\n")
    return content


def write_content_into_new_file(file_name: str, content: list) -> None:
    with open(file_name, "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.writelines(content)


def create_file() -> None:
    command_line = sys.argv
    if "-f" in command_line:
        if "-d" in command_line:
            if command_line.index("-d") < command_line.index("-f"):
                path_ = os.path.join(
                    *command_line[command_line.index("-d") + 1
                                  :command_line.index("-f")]
                )
            else:
                path_ = os.path.join(
                    *command_line[command_line.index("-d") + 1::]
                )
            os.makedirs(path_)
            os.chdir(path_)
        file_name = command_line[command_line.index("-f") + 1]
        content = create_content_for_new_file()
        write_content_into_new_file(file_name, content)
    elif "-d" in command_line:
        path_ = os.path.join(*command_line[command_line.index("-d") + 1::])
        os.makedirs(path_)


if __name__ == "__main__":
    create_file()
