import os
import sys
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    dir_parts: list[str] = []
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
            i += 1
    return dir_parts, file_name


def get_content_lines() -> list[str]:
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def create_file(dir_parts: list[str], file_name: str, lines: list[str]) -> str:
    dir_path = os.path.join(*dir_parts) if dir_parts else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name
    file_exists = os.path.exists(file_path)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n")
        output_file.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, 1):
            output_file.write(f"{idx} {line}\n")

    return file_path


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(
            "Usage: python create_file.py -d dir1 dir2 ... -f filename"
        )
        return

    dir_parts, file_name = parse_args(args)
    if not file_name:
        print("Missing -f filename argument.")
        return

    lines = get_content_lines()
    file_path = create_file(dir_parts, file_name, lines)
    print(f"File created/updated at: {file_path}")


if __name__ == "__main__":
    main()
