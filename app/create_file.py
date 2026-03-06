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


def parse_arguments(args: list[str]) -> tuple[list[str], str | None]:
    dirs = []
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")

        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dirs.append(arg)

        if dirs:
            dir_path = os.path.join(*dirs)
            os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")

        if (
                f_index + 1 < len(args)
                and not args[f_index + 1].startswith("-")
        ):
            file_name = args[f_index + 1]

    return dirs, file_name


def main() -> None:
    args = sys.argv[1:]

    dirs, file_name = parse_arguments(args)

    dir_path = ""

    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

    if not file_name:
        return

    lines = get_content()

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    write_to_file(file_path, lines)


if __name__ == "__main__":
    main()
