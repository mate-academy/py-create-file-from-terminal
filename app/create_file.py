import os
import sys
from datetime import datetime


def parse_path(arguments: list) -> list | None:
    try:
        d_index = arguments.index("-d")
    except ValueError:
        return None

    path_list = []

    for item in range(d_index + 1, len(arguments)):
        if arguments[item].startswith("-"):
            break
        path_list.append(arguments[item])

    return path_list


def parse_file_name(arguments: list) -> str:
    file_name = "file.txt"
    try:
        f_index = arguments.index("-f")
        file_name = arguments[f_index + 1]
    except ValueError:
        pass

    return file_name


def create_file(
        directory: list,
        filename: str,
        content_lines: list
) -> None:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)

    print(directory)

    if directory:
        dir_path = os.path.join(script_directory, *directory)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, filename)
    else:
        file_path = filename

    with open(file_path, "a") as file:
        if os.path.exists(file_path):
            file.write("\n\n" + timestamp + "\n")
        else:
            file.write(timestamp + "\n")

        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    arguments = sys.argv[1:]
    if not arguments:
        sys.exit(1)

    file_name = parse_file_name(arguments)
    path = parse_path(arguments)

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    create_file(path, file_name, content_lines)


if __name__ == "__main__":
    main()
