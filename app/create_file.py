import sys
import os
from datetime import datetime


def create_directory(dir_parts: list[str]) -> str:
    path = os.path.join(*dir_parts)
    os.makedirs(path, exist_ok=True)
    return path


def prompt_for_content() -> list[str]:
    lines: list[str] = []
    line_num = 1
    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        lines.append(f"{line_num} {user_input}")
        line_num += 1
    return lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for line in content_lines:
            f.write(line + "\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        return

    dir_parts: list[str] = []
    file_name: str = ""

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue
        if args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            continue
        i += 1

    if not dir_parts:
        dir_parts = []

    if not file_name:
        if dir_parts:
            create_directory(dir_parts)
        return

    base_path = os.getcwd()
    if dir_parts:
        base_path = create_directory(dir_parts)

    file_path = os.path.join(base_path, file_name)
    content = prompt_for_content()
    write_to_file(file_path, content)


if __name__ == "__main__":
    main()
