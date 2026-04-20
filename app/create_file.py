import sys
import os
from datetime import datetime


def get_content() -> list[str]:
    lines = []
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    return lines


def main() -> None:
    args = sys.argv[1:]

    directory_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                directory_parts.append(args[i])
                i += 1
            continue

        if args[i] == "-f":
            if i + 1 < len(args):
                file_name = args[i + 1]
            i += 2
            continue

        i += 1

    directory = ""
    if directory_parts:
        directory = os.path.join(*directory_parts)
        os.makedirs(directory, exist_ok=True)

    if not file_name:
        return

    file_path = os.path.join(directory, file_name) if directory else file_name

    content_lines = get_content()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")
        for line in content_lines:
            file.write(f"{line}\n")


main()
