import os
import sys
from datetime import datetime


def get_content() -> list[str]:
    content = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content.append(line)

    return content


def main() -> None:
    args = sys.argv[1:]

    filename = None
    directories = []

    if "-f" in args:
        file_index = args.index("-f")
        filename = args[file_index + 1]

    if "-d" in args:
        dir_index = args.index("-d")

        if "-f" in args:
            file_index = args.index("-f")

            if dir_index < file_index:
                directories = args[dir_index + 1:file_index]
            else:
                directories = args[dir_index + 1:]
        else:
            directories = args[dir_index + 1:]

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if filename is None:
        return

    file_path = os.path.join(directory_path, filename)

    content = get_content()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for number, line in enumerate(content, start=1):
            file.write(f"{number} {line}\n")


main()
