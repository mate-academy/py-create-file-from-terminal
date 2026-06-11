import sys
import os
from datetime import datetime


def get_content() -> list:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


def main() -> None:
    args = sys.argv[1:]

    directory_path = ""
    file_name = None

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if "-d" in args:
        d_index = args.index("-d")

        directories = []

        for item in args[d_index + 1:]:
            if item.startswith("-"):
                break
            directories.append(item)

        if directories:
            directory_path = os.path.join(*directories)
            os.makedirs(directory_path, exist_ok=True)

    if file_name is None:
        return

    lines = get_content()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = [timestamp]

    for number, line in enumerate(lines, start=1):
        content.append(f"{number} {line}")

    block = "\n".join(content)

    if directory_path:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n\n")
            file.write(block)
    else:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(block)


main()
