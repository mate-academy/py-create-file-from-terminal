import sys
import os
from datetime import datetime


def read_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break

        lines.append(line)

    return lines


def write_content(path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(path) else "w"

    with open(path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(timestamp + "\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        return

    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-f", "-d"):
                dir_parts.append(args[i])
                i += 1
            continue

        if args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            continue

    directory = ""
    if dir_parts:
        directory = os.path.join(*dir_parts)
        os.makedirs(directory, exist_ok=True)

    if not file_name:
        return

    file_path = os.path.join(directory, file_name) if directory else file_name

    lines = read_content()
    write_content(file_path, lines)


if __name__ == "__main__":
    main()
