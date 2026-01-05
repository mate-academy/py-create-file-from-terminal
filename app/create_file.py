import sys
import os
import datetime


def parse_arguments(arguments: list) -> tuple:
    directories = []
    filename = None

    index_d = arguments.index("-d") if "-d" in arguments else None
    index_f = arguments.index("-f") if "-f" in arguments else None

    if index_d is not None:
        if index_f is not None and index_f > index_d:
            directories = arguments[index_d + 1:index_f]
        else:
            directories = arguments[index_d + 1:]

    if index_f is not None:
        if index_f + 1 < len(arguments):
            next_argument = arguments[index_f + 1]
            if next_argument.startswith("-"):
                raise ValueError("'-f' flag requires a valid filename, not another flag")
            filename = next_argument
        else:
            raise ValueError("'-f' flag requires a filename")

    return directories, filename


def create_directories(directories: list) -> None:
    if not directories:
        return
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def collect_lines() -> list:
    lines = []
    while True:
        user_text = input("Enter content line: ")
        if user_text.lower() == "stop":
            break
        lines.append(user_text)

    return lines


def write_to_file(directories: list, filename: str, lines: list) -> None:
    if filename is None:
        raise ValueError("Filename must be provided")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_path = os.path.join(
        *directories,
        filename
    )if directories else filename

    with open(file_path, "a") as file:
        file.write(current_time + "\n")
        for page_number, line in enumerate(lines, 1):
            file.write(f"{page_number} {line}\n")
        file.write("\n")


def main() -> None:
    arguments = sys.argv[1:]
    directories, filename = parse_arguments(arguments)

    create_directories(directories)

    if filename:
        lines = collect_lines()
        write_to_file(directories, filename, lines)


if __name__ == "__main__":
    main()
