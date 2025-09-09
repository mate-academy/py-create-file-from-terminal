import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def parse_arguments(args: List) -> Tuple[List, Optional[str]]:
    directory_parts = []
    filename = None

    argument_index = 0
    while argument_index < len(args):
        if args[argument_index] == "-d":
            argument_index += 1
            while argument_index < len(args) and args[argument_index] != "-f":
                directory_parts.append(args[argument_index])
                argument_index += 1
            continue

        if args[argument_index] == "-f":
            argument_index += 1
            if argument_index < len(args):
                filename = args[argument_index]
                argument_index += 1
            continue

        argument_index += 1

    return directory_parts, filename


def create_directory(directory_parts: List) -> str:
    if not directory_parts:
        return "."

    directory_path = os.path.join(*directory_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_content_from_user() -> List:
    content_lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        content_lines.append(user_input)

    return content_lines


def write_content_to_file(file_path: str, content_lines: List) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists_and_not_empty = (os.path.exists(file_path)
                                 and os.path.getsize(file_path) > 0)

    with open(file_path, "a") as target_file:
        if file_exists_and_not_empty:
            target_file.write("\n")

        target_file.write(f"{timestamp}\n")
        for line_number, content_line in enumerate(content_lines, 1):
            target_file.write(f"Line{line_number} {content_line}\n")


def main() -> None:
    command_args = sys.argv[1:]

    directory_parts, filename = parse_arguments(command_args)
    directory_path = create_directory(directory_parts)

    if filename:
        file_path = os.path.join(directory_path, filename)
        content_lines = get_content_from_user()
        write_content_to_file(file_path, content_lines)
        print(f"File created/updated: {file_path}")
        return

    if directory_parts:
        print(f"Directory created: {directory_path}")


if __name__ == "__main__":
    main()
