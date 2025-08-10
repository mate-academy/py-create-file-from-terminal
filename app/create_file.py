import os
import sys
from datetime import datetime


def main() -> None:
    directories = parse_command("-d")
    if directories:
        os.makedirs(os.path.join(*directories), exist_ok=True)

    filenames = parse_command("-f")
    if filenames:
        filename = filenames[0]
        write_to_file(directories, filename)


def parse_command(flag: str) -> list | bool:
    if flag not in sys.argv:
        return False
    args = []
    for i in range(sys.argv.index(flag) + 1, len(sys.argv)):
        if sys.argv[i].startswith("-"):
            break
        args.append(sys.argv[i])
    return args


def write_to_file(directories: list, filename: str) -> None:
    file_path = os.path.join(*directories, filename)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    with open(file_path, "a") as source_file:
        source_file.write(f"{current_date}\n")
        for i in range(len(lines)):
            source_file.write(f"{i + 1} {lines[i]}\n")
        source_file.write("\n")


if __name__ == "__main__":
    main()
