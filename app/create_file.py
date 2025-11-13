import sys
import os
from datetime import datetime


def read_content_from_terminal() -> list[str]:
    lines = []
    counter = 1
    while True:
        user_input = input("Enter content line: ")
        if user_input.strip().lower() == "stop":
            break
        lines.append(f"{counter} {user_input}")
        counter += 1
    return lines


def write_content_to_file(path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n")
        for line in lines:
            f.write(f"{line}\n")
        f.write("\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python create_file.py -d <dirs> -f <file>")
        print("  python create_file.py -f <file>")
        print("  python create_file.py -d <dirs>")
        return

    args = sys.argv[1:]
    directory_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directory_parts.append(args[i])
                i += 1
            continue

        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
                continue
            else:
                print("Error: -f flag used but filename not provided.")
                return

        else:
            print(f"Unknown argument: {args[i]}")
            return

    if directory_parts:
        dir_path = os.path.join(*directory_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""

    if file_name is None:
        print("Directory created. No file requested (-f flag missing).")
        return

    file_path = os.path.join(dir_path, file_name)
    content_lines = read_content_from_terminal()
    write_content_to_file(file_path, content_lines)

    print(f"File created/updated at: {file_path}")
