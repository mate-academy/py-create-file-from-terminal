import sys
import os
from datetime import datetime

"""
os.path.exists() — checks whether the specified path exists or not;
os.path.join() — intelligently joins one or more path components.
"""


def get_path_from_command_line() -> str | None:
    path = ""
    command_line = sys.argv

    if "-f" not in command_line and "-d" not in command_line:
        raise SyntaxError("You should use at least one flag")

    if "-d" in command_line:
        flag_index = command_line.index("-d")
        try:
            path = os.path.join(
                command_line[flag_index + 1],
                command_line[flag_index + 2]
            )
            os.makedirs(path, exist_ok=True)
        except IndexError:
            raise SyntaxError("Invalid input")

    if "-f" in command_line:
        flag_index = command_line.index("-f")
        try:
            path = os.path.join(
                path,
                command_line[flag_index + 1],
            )
        except IndexError:
            raise SyntaxError("Invalid input")

    return path


def write_file(file_path: str) -> None:
    mode = "a" if os.path.exists(file_path) else "w"
    try:
        with open(file_path, mode) as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            file.write("\n")
            line_number = 1
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1
            file.write("\n")
    except PermissionError:
        print("Directory created")


if __name__ == "__main__":
    write_file(get_path_from_command_line())
