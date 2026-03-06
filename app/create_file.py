import sys
import os
from datetime import datetime


def get_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n")

        file.write(f"{timestamp}\n")

        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else len(args)
        dirs = args[d_index + 1:f_index]

        if dirs:
            dir_path = os.path.join(*dirs)
            os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if not file_name:
        return

    lines = get_content()

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    write_to_file(file_path, lines)


if __name__ == "__main__":
    main()
