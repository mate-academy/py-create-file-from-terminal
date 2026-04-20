import sys
import os
from datetime import datetime


def parse_args() -> tuple:
    args = sys.argv[1:]

    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return directories, file_name


def create_directories(directories: list) -> list:
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    return None


def get_user_input() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_file(file_name: str, lines: list) -> None:
    with open(file_name, "a") as file:
        time_stamp = datetime.now()
        file.write(time_stamp.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        for index, line in enumerate(lines, 1):
            file.write(f"{index} {line}\n")
        file.write("\n")


def main() -> None:
    directories, file_name = parse_args()

    dir_path = create_directories(directories)

    if file_name:
        lines = get_user_input()

        if dir_path:
            file_name = os.path.join(dir_path, file_name)

        write_file(file_name, lines)


if __name__ == "__main__":
    main()
