import sys
import os
from datetime import datetime
from typing import List


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def prompt_for_lines() -> List[str]:
    lines: List[str] = []
    count = 1
    while True:
        line = input("Enter content line: ")
        if line.strip() == "stop":  # Case-sensitive check
            break
        lines.append(f"{count} {line}")
        count += 1
    return lines


def write_to_file(file_path: str, lines: List[str]) -> None:
    timestamp = get_timestamp()
    content = [timestamp] + lines

    needs_separator = (os.path.exists(file_path)
                       and os.path.getsize(file_path) > 0)

    with open(file_path, "a") as f:
        if needs_separator:
            f.write("\n")
        f.write("\n".join(content) + "\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  -d <dir1> <dir2> ... to specify directories")
        print("  -f <filename> to specify a file")
        return

    dir_parts: List[str] = []
    file_name: str | None = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                print("Error: -f flag provided but no filename given.")
                return
        else:
            print(f"Unknown argument: {args[i]}")
            return

    if dir_parts:
        dir_path = os.path.join(os.getcwd(), *dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = os.getcwd()

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        lines = prompt_for_lines()
        if lines:
            write_to_file(file_path, lines)
            print(f"Content written to: {file_path}")
    else:
        if dir_parts:
            print(f"Directory created: {os.path.join(*dir_parts)}")


if __name__ == "__main__":
    main()
