import os
import sys
from datetime import datetime


def parse_arguments(args: list[str]) -> tuple[list[str], str]:
    directories: list[str] = []
    filename: str = ""
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            if i + 1 < len(args):
                filename = args[i + 1]
                i += 2
            else:
                print("Error: -f requires a filename.")
                sys.exit(1)
        else:
            i += 1
    return directories, filename


def make_directories(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directories: {e}")
        sys.exit(1)


def get_user_content() -> list[str]:
    lines: list[str] = []
    print("Enter content (type 'stop' to finish):")
    while True:
        line = input("> ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(target_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(target_path)

    try:
        with open(target_path, "a", encoding="utf-8") as f:
            if file_exists:
                f.write("\n")

            f.write(f"[{timestamp}]\n")
            for idx, line in enumerate(lines, 1):
                f.write(f"{idx}. {line}\n")
    except IOError as e:
        print(f"Error writing to file: {e}")


def main() -> None:
    raw_args: list[str] = sys.argv[1:]

    if not raw_args:
        print("Usage: python script.py -d dir1 dir2 -f file.txt")
        return

    dirs, name = parse_arguments(raw_args)

    if not name:
        print("Error: Filename (-f) is required.")
        return

    if dirs:
        path = os.path.join(dirs[0], *dirs[1:])
    else:
        path = "."

    if path != ".":
        make_directories(path)

    content = get_user_content()
    if not content:
        print("No content provided. Exiting.")
        return

    full_path = os.path.join(path, name)
    write_to_file(full_path, content)
    print(f"Success: {full_path}")


if __name__ == "__main__":
    main()
