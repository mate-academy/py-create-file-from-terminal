import os
import sys
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def collect_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: list[str]) -> str:
    timestamp = get_timestamp()
    numbered_lines = [f"{i + 1} {line}" for i, line in enumerate(lines)]
    return f"{timestamp}\n" + "\n".join(numbered_lines) + "\n"


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_path = ""
    file_name = ""
    content_mode = False

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            dir_parts = []
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            dir_path = os.path.join(*dir_parts)
            os.makedirs(dir_path, exist_ok=True)
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                content_mode = True
                i += 1
            else:
                print("Error: No file name specified after -f")
                return
        else:
            print(f"Unknown flag or argument: {args[i]}")
            return

    if not content_mode:
        return

    full_path = os.path.join(dir_path, file_name) if dir_path else file_name

    lines = collect_content()
    if not lines:
        print("No content to write.")
        return

    content = format_content(lines)

    with open(full_path, "a", encoding="utf-8") as f:
        f.write(content)

    print(f"File written to: {full_path}")


if __name__ == "__main__":
    main()
