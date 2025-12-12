import sys
import os
from datetime import datetime


def content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")
        file.write("\n")


def main() -> None:
    args = sys.argv[1:]
    directory = []
    file_name = None
    flags = 0

    while flags < len(args):
        if args[flags] == "-d":
            flags += 1
            while flags < len(args) and not args[flags].startswith("-"):
                directory.append(args[flags])
                flags += 1
            continue

        if args[flags] == "-f":
            if flags + 1 < len(args):
                file_name = args[flags + 1]
                flags += 2
                continue
            else:
                print("Error: -f must be followed by file name")
                return
        flags += 1

    if directory:
        dir_path = os.path.join(*directory)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if not file_name:
        if directory:
            print(f"Directories created at: {dir_path}")
            return
        else:
            print("Error: no file name provided. Use -f <file>")
            return

    full_path = os.path.join(dir_path, file_name)

    write_to_file(full_path, content())

    print(f"File created/updated at: {full_path}")


if __name__ == "__main__":
    main()
