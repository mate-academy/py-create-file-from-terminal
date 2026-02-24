import sys
import os
from datetime import datetime
from os import mkdir


def parse_arguments() -> tuple[str | None, str | None]:
    args = sys.argv[1:]

    path_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == '-d':
            i += 1
            while i < len(args) and args[i] != '-f':
                path_parts.append(args[i])
                i += 1
        elif args[i] == '-f':
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    if path_parts:
        directory_path = os.path.join(*path_parts)
    else:
        directory_path = None

    return directory_path, file_name

def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def get_content_from_user() -> list[str]:
    write_list = []
    while True:
        user_input = input("Enter content line (type 'stop' to finish): ")
        if user_input == "stop":
            break
        write_list.append(user_input)
    return write_list

def prepare_content(lines: list[str]) -> str:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    output_lines = [timestamp]

    for number, line in enumerate(lines, start=1):
        output_lines.append(f"{number} {line}")

    return "\n".join(output_lines) + "\n\n"

def write_to_file(file_path: str, content: str) -> None:
    with open(file_path, "a") as file:
        file.write(content)

        file.close()

def main():
    directory_path, file_name = parse_arguments()

    if directory_path:
        create_directory(directory_path)

    if file_name:
        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        lines = get_content_from_user()
        content = prepare_content(lines)
        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
