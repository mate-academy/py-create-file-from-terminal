import os
import sys
from datetime import datetime


def get_content_from_user() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_content_to_file(
        target_path: str,
        file_name: str,
        content: list
) -> None:
    full_file_path = os.path.join(target_path, file_name)
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_file_path, "a", encoding="utf-8") as output_file:
        output_file.write(f"{current_timestamp}\n")
        for line_number, text in enumerate(content, start=1):
            output_file.write(f"{line_number} {text}\n")


def main() -> None:
    command_args = sys.argv[1:]
    if not command_args:
        return

    directory_parts = []
    file_name = None

    arg_index = 0
    while arg_index < len(command_args):
        if command_args[arg_index] == "-d":
            arg_index += 1
            while arg_index < len(command_args) and not command_args[arg_index].startswith("-"):
                directory_parts.append(command_args[arg_index])
                arg_index += 1
            continue

        if command_args[arg_index] == "-f":
            if arg_index + 1 < len(command_args):
                file_name = command_args[arg_index + 1]
                arg_index += 2
                continue

        arg_index += 1

    target_directory = os.path.join(*directory_parts) if directory_parts else "."

    if directory_parts:
        os.makedirs(target_directory, exist_ok=True)

    if file_name:
        user_content = get_content_from_user()
        write_content_to_file(target_directory, file_name, user_content)


if __name__ == "__main__":
    main()
