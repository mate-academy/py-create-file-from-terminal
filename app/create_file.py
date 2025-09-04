import sys
import os
from datetime import datetime


def get_input_lines() -> list:
    input_lines = []
    line_number = 1
    while True:
        user_input = input("Enter content: ")
        if user_input.strip().lower() == "stop":
            break
        input_lines.append(f"{line_number} {user_input}")
        line_number += 1
    return input_lines


def write_to_file(lines: list, file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp] + lines
    content_text = "\n".join(content) + "\n\n"

    with open(file_path, "a") as file:
        file.write(content_text)


def main() -> None:
    args = sys.argv[1:]
    print(args)
    if not args:
        return
    dir_path = ""
    file_name = ""
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            dir_parts = []
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
                dir_path = os.path.join(*dir_parts)
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                return
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    if file_name:
        full_path = os.path.join(dir_path, file_name) \
            if dir_path else file_name
        lines = get_input_lines()
        write_to_file(lines, full_path)


if __name__ == "__main__":
    main()
