import os
import sys
from datetime import datetime


def create_directory(command: list[str]) -> str:
    path_start = command.index("-d") + 1
    path_end = None
    if "-f" in command:
        path_end = command.index("-f")
    return os.path.join(*command[path_start: path_end])


def create_file(file_: str) -> None:
    if os.path.isfile(file_):
        open_mode = "a"
    else:
        open_mode = "w"
    with open(file_, open_mode) as file:
        date_time_now = datetime.datetime.utcnow()
        file.write(date_time_now.strftime("%Y-%m-%d %H:%M:%S" + "\n"))
        content = None
        line_number = 1
        while content != "stop":
            content = input("Enter content line: ")
            if content != "stop":
                file.write(f"{line_number} {content}" + "\n")
                line_number += 1
            else:
                file.write("\n")


if __name__ == "__main__":
    command_ = sys.argv
    if "-d" in command_:
        path_dir = create_directory(command_)
        os.makedirs(path_dir, exist_ok=True)
    if "-f" in command_:
        file_name = command_[command_.index("-f") + 1]
        if "-d" in command_:
            file_name = os.path.join(path_dir, file_name)
        create_file(file_name)
