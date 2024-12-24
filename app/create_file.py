import os
from sys import argv
from datetime import datetime


def create_directory(path_components: list) -> str:
    path = os.path.join(*path_components)
    os.makedirs(path, exist_ok=True)
    return path


def write_file(file_path: str, append: bool = False) -> None:
    mode = "a" if append else "w"
    format_string = "%Y-%m-%d %H:%M:%S"
    with open(file_path, mode) as source_file:
        source_file.write(f"\n{datetime.now().strftime(format_string)}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ").strip()
            if content.lower() == "stop":
                break
            source_file.write(f"{line_number} {content}\n")
            line_number += 1


def parse_directory(arguments: list) -> list:
    index = arguments.index("-d")
    components = []
    for arg in arguments[index + 1 :]:
        if arg.startswith("-"):
            break
        components.append(arg)
    return components


def parse_file(arguments: list) -> str:
    index = arguments.index("-f")
    return arguments[index + 1]


def main() -> None:
    args = argv[1:]

    create_dir = "-d" in args
    create_file = "-f" in args

    dir_path = ""
    if create_dir:
        directory_path = parse_directory(args)
        dir_path = create_directory(directory_path)

    if create_file:
        file_name = parse_file(args)
        file_path = os.path.join(dir_path, file_name) if create_dir \
            else file_name
        write_file(file_path, append=os.path.exists(file_path))


if __name__ == "__main__":
    main()
