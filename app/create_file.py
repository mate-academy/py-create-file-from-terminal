import os
import sys
from datetime import datetime


def create_directories(directories: list[str]) -> str:
    if not directories:
        return ""

    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)

    return directory_path


def create_file(directory_path: str, filename: str) -> None:
    file_path = os.path.join(directory_path, filename)

    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines_to_write = [
        f"{timestamp}\n",
        *[
            f"{number} {line}\n"
            for number, line in enumerate(content_lines, start=1)
        ],
    ]

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        lines_to_write.insert(0, "\n")

    with open(file_path, "a") as file:
        file.writelines(lines_to_write)


def main() -> None:
    _, *args = sys.argv

    directories = []
    filename = None

    if "-f" in args:
        file_flag_index = args.index("-f")

        if file_flag_index + 1 < len(args):
            filename = args[file_flag_index + 1]

    if "-d" in args:
        directory_flag_index = args.index("-d")
        directory_end_index = len(args)

        if "-f" in args:
            file_flag_index = args.index("-f")

            if file_flag_index > directory_flag_index:
                directory_end_index = file_flag_index

        directories = args[directory_flag_index + 1:directory_end_index]

    directory_path = create_directories(directories)

    if filename:
        create_file(directory_path, filename)


if __name__ == "__main__":
    main()
elif __name__ == "<run_path>":
    main()
