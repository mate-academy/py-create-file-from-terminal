import sys
import os
from datetime import datetime


def parse_args(argv: list[str]) -> tuple[list[str], str | None]:

    dirs = []
    filename = None

    i = 1

    while i < len(argv):
        if argv[i] == "-d":
            i += 1
            while i < len(argv) and not argv[i].startswith("-"):
                dirs.append(argv[i])
                i += 1
        elif argv[i] == "-f":
            i += 1
            if i < len(argv):
                filename = argv[i]
                i += 1
        else:
            i += 1

    return dirs, filename


def read_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")
        file.write("\n")


def main() -> None:
    dirs, filename = parse_args(sys.argv)

    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = os.getcwd()

    if not filename:
        return

    file_path = os.path.join(dir_path, filename)
    content = read_content()
    write_to_file(file_path, content)


if __name__ == "__main__":
    main()
