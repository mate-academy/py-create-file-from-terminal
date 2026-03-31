import sys
import os
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    dirs: list[str] = []
    filename: str | None = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ["-d", "-f"]:
                dirs.append(args[i])
                i += 1

        elif args[i] == "-f":
            if i + 1 < len(args):
                filename = args[i + 1]
                i += 2
            else:
                print("Error: filename not provided")
                sys.exit()
        else:
            i += 1

    return dirs, filename


def create_dirs(dirs: list[str]) -> str:
    if not dirs:
        return ""

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def get_user_input() -> list[str]:
    lines: list[str] = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    return lines


def write_file(path: str, filename: str, lines: list[str]) -> None:
    file_path = os.path.join(path, filename) if path else filename

    file_exists = os.path.exists(file_path)
    has_content = False

    if file_exists:
        with open(file_path, "r", encoding="utf-8") as check_file:
            has_content = bool(check_file.read().strip())

    content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

    for i, line in enumerate(lines, 1):
        content += f"{i} {line}\n"

    if has_content:
        content = "\n" + content

    content += "\n"

    with open(file_path, "a", encoding="utf-8") as output_file:
        output_file.write(content)

    print(f"File created/updated: {file_path}")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d dir1 dir2 -f filename.txt")
        return

    dirs, filename = parse_args(args)
    path = create_dirs(dirs)

    if not filename:
        print(f"Directories created: {path}")
        return

    lines = get_user_input()
    write_file(path, filename, lines)


if __name__ == "__main__":
    main()
