import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    directories = []
    filename = None

    if "-d" in args:
        d_index = args.index("-d")
        end_index = args.index("-f") if "-f" in args else len(args)
        directories = args[d_index + 1:end_index]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    directory = os.path.join(*directories) if directories else "."

    if directories:
        os.makedirs(directory, exist_ok=True)

    if filename is None:
        return

    filepath = os.path.join(directory, filename)

    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as file:
        if os.path.getsize(filepath) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


if __name__ == "__main__":
    main()
