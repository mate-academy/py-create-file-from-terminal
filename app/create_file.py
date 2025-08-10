import os
import sys
import datetime

from typing import LiteralString

command = sys.argv


def create_path(command_sting: list[str]) -> LiteralString | str | bytes:
    if "-d" in command:
        dirs = command[command.index("-d") + 1: command.index("-f")] \
            if "-f" in command else command[command.index("-d") + 1:]
        path_dirs = os.path.join(*dirs)
        return path_dirs

    return ""


def create_dirs_file() -> None:
    path_dirs = create_path(command)
    os.makedirs(path_dirs, exist_ok=True)

    if "-f" in command:
        file_path = os.path.join(path_dirs, command[command.index("-f") + 1])
        with (open(file_path, "a+") as file):
            current_time = datetime.datetime.now()
            file.write(str(current_time.strftime("%Y-%m-%d %H:%M:%S")) + "\n")
            for num_of_row, file_text in enumerate(
                    iter(input, "stop"), start=1
            ):
                file.write(f"{num_of_row} {file_text}\n")


if __name__ == "__main__":
    create_dirs_file()
