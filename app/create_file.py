import sys
import os
from datetime import datetime


def get_command_flags() -> tuple[list, list]:
    command = sys.argv[1:]
    size = len(command)
    d_index, f_index = size, size

    for i in range(size):
        if command[i] == "-f":
            f_index = i
        elif command[i] == "-d":
            d_index = i

    if d_index < f_index:
        # f_args = [] if flag does not exist
        return (command[d_index + 1:min(f_index, size)],
                command[f_index + 1:size])
    else:
        # d_args = [] if flag does not exist
        return (command[d_index + 1:size],
                command[f_index + 1:min(d_index, size)])


def create_path(
        directories: list[str],
        file_name: list[str]
) -> str:
    path = ""

    if directories:
        path = os.path.join(*directories)
        if not os.path.exists(path):
            os.makedirs(path)

    return os.path.join(path, " ".join(file_name))


def create_file() -> None:
    with open(create_path(*get_command_flags()), "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_pointer = 1

        while True:
            content = input("Enter content line: ")

            if content == "stop":
                break

            file.write(f"{line_pointer} {content}\n")
            line_pointer += 1


if __name__ == "__main__":
    create_file()
