import os
import sys
from datetime import datetime


def make_direction(commands: list) -> str:
    if "-d" in commands:
        if "-f" in commands:
            dirs = os.path.join(
                *commands[commands.index("-d") + 1: commands.index("-f")]
            )
            os.makedirs(dirs)
            os.chdir(dirs)
            return commands[commands.index("-f") + 1]
        return os.makedirs(os.path.join(*commands[commands.index("-d") + 1:]))
    return commands[commands.index("-f") + 1]


def working_with_file(file_name: str) -> None:
    with open(
            f"{file_name}", "a" if os.path.exists(file_name) else "w"
    ) as file:
        count_line: int = 0
        file.writelines(datetime.now().strftime("\n%Y-%m-%d %H:%M:%S\n"))
        while True:
            count_line += 1
            data = input("Enter content line:")
            if data == "stop":
                break
            file.writelines(f"{count_line} {data}\n")


if __name__ == "__main__":
    file_name = make_direction(sys.argv)
    if file_name:
        working_with_file(file_name)
