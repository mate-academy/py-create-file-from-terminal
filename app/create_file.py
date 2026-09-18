import os
import sys
from datetime import datetime


def parse_arguments(args: list[str]) -> tuple[list[str], str | None]:
    directories: list[str] = []
    file_name: str | None = None

    flag_positions = sorted(i for i, arg in enumerate(
        args) if arg in ("-d", "-f"))

    if "-d" in args:
        d_index = args.index("-d")
        next_flag_index = next((pos for pos in flag_positions if pos > d_index
                                ), len(args))
        directories = args[d_index + 1:next_flag_index]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
    return directories, file_name


def read_content_line() -> list[str]:
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def build_content_block(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numberet_lines = [f"{index} {line}" for index, line in enumerate(
        lines, start=1)]
    return timestamp + "\n" + "\n".join(numberet_lines)


def write_file(file_path: str, content_block: str) -> None:
    file_exsist_and_not_empty = os.path.exists(file_path
                                               ) and os.path.getsize(file_path
                                                                     ) > 0

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exsist_and_not_empty:
            file.write("\n\n")
        file.write(content_block)


def main() -> None:
    args = sys.argv[1:]
    if "-d" not in args and "-f" not in args:
        print("Error: you must pass at least one of the flags -d or -f")
        return
    directories, file_name = parse_arguments(args)

    target_directory = ""
    if directories:
        target_directory = os.path.join(*directories)
        os.makedirs(target_directory, exist_ok=True)
        print(f"Directory created: {target_directory}")

    if not file_name:
        return

    file_path = os.path.join(target_directory, file_name)

    content_lines = read_content_line()
    content_block = build_content_block(content_lines)
    write_file(file_path, content_block)

    print(f"File created/updated: {file_path}")


main()
