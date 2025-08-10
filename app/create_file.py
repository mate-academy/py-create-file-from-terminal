import os
import sys
from datetime import datetime


def create_path(path: list[str]) -> str:
    index = path.index("-d")
    file_path = path[index + 1:]
    full_path = os.path.join(*[os.getcwd(), *file_path])
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def create_file(command: list[str]) -> None:
    file_name = None
    full_path = None
    if "-f" in command:
        index = command.index("-f")
        file_name = command[index + 1]
        full_path = file_name

    if "-d" in command and "-f" in command:
        full_path = os.path.join(create_path(command), file_name)

    if full_path is None:
        if "-d" in command:
            create_path(command)
            return

    mode = "a" if os.path.exists(full_path) else "w"

    with open(full_path, mode) as file:
        file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        line_char = 0
        while True:
            line_char += 1
            input_data = str((input("Enter content line: ")))
            if input_data == "stop":
                break
            file.write(f"{line_char} {input_data}\n")
        file.write("\n")


if __name__ == "__main__":
    create_file(sys.argv)
