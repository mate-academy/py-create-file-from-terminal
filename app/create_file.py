import os
import sys
import datetime
from typing import Any


def create_directory(path_parts: Any) -> None:
    dir_path = os.path.join(*path_parts)
    os.makedirs(dir_path, exist_ok=True)


def create_file_with_content(file_name: str) -> None:
    output_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        output_lines.append(line)

    if os.path.exists(file_name):
        with open(file_name, "a") as a:
            a.write("\n" + datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S") + "\n"
                       )
            for i, line in enumerate(output_lines, start=1):
                a.write(f"{i} {line}\n")
    else:
        with open(file_name, "w") as w:
            w.write(datetime.datetime.now().strftime(
                "%Y-%m""-%d %H:%M:%S") + "\n"
                       )
            for i, line in enumerate(output_lines, start=1):
                w.write(f"{i} {line}\n")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py "
              "[-d path_parts] -f file_name")
        sys.exit(1)

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        path_parts = sys.argv[d_index + 1:]

        create_directory(path_parts)

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]

        create_file_with_content(file_name)


if __name__ == "__main__":
    main()
