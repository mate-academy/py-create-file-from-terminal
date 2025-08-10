import sys
import os
from datetime import datetime


def create_file(directory: str, name: str) -> str:
    if directory:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, name)
    else:
        file_path = name

    if not os.path.exists(file_path):
        open(file_path, "w").close()
    return file_path


def add_content_to_file(file_path: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"\n{timestamp}\n")
        for count, line in enumerate(lines, start=1):
            file.write(f"{count} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    directory = ""
    file_name = ""

    if "-d" in args:
        dir_index = args.index("-d") + 1
        while dir_index < len(args) and not args[dir_index].startswith("-"):
            directory = os.path.join(directory, args[dir_index])
            dir_index += 1

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index < len(args):
            file_name = args[file_index]

    if not file_name:
        print("Error: File name must be specified with the -f flag.")
        return

    file_path = create_file(directory, file_name)
    add_content_to_file(file_path)


if __name__ == "__main__":
    main()
