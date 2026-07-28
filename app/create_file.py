import os
import sys
from datetime import datetime


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


def write_file(path: str, lines: list[str]) -> None:
    mode = "a" if os.path.exists(path) else "w"

    with open(path, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write("\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    directory = ""
    filename = ""

    if "-f" in args:
        filename = args[args.index("-f") + 1]

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")

            if d_index < f_index:
                dirs = args[d_index + 1:f_index]
            else:
                dirs = args[d_index + 1:]
        else:
            dirs = args[d_index + 1:]

        if dirs:
            directory = os.path.join(*dirs)
            os.makedirs(directory, exist_ok=True)

    if filename:
        file_path = os.path.join(directory, filename)
        lines = get_content()
        write_file(file_path, lines)


main()
