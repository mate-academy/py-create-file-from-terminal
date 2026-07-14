import sys
import os
import datetime


def parse_arguments(args: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        # directories go from right after "-d" up to the next flag (or end)
        end_index = len(args)
        for flag in ("-f",):
            if flag in args and args.index(flag) > d_index:
                end_index = min(end_index, args.index(flag))
        directories = args[d_index + 1:end_index]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return directories, file_name


def create_directories(directories: list[str]) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def collect_content_lines() -> list[str]:
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        lines.append(user_input)
    return lines


def write_content_to_file(file_path: str, lines: list[str]) -> None:
    is_empty = not os.path.exists(file_path) or os.path.getsize(file_path) == 0

    with open(file_path, "a") as f:
        if not is_empty:
            f.write("\n")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{date}\n")
        for index, line in enumerate(lines, start=1):
            f.write(f"{index} {line}\n")


def main() -> None:
    args = sys.argv
    directories, file_name = parse_arguments(args)

    if directories:
        create_directories(directories)

    if file_name:
        file_path = os.path.join(*directories, file_name) \
            if directories else file_name
        content_lines = collect_content_lines()
        write_content_to_file(file_path, content_lines)


main()
