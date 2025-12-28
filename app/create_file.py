import sys
import os
from datetime import datetime


def get_content() -> list[str]:
    """Read lines from user until 'stop' is entered."""
    lines = []
    counter = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def write_content(file_path: str) -> None:
    """Write timestamp and numbered content lines to file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = get_content()

    with open(file_path, "a", encoding="utf-8") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write(timestamp + "\n")
        f.write("\n".join(lines))


def main() -> None:
    """Parse arguments and create directories/files as required."""
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d <dirs...> -f <filename>")
        sys.exit(1)

    dir_parts = []
    file_name = None

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
                print("Error: -f flag requires file name")
                sys.exit(1)
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    # Build directory path
    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        write_content(file_path)
        print(f"File created/updated at: {file_path}")
    else:
        print(f"Directory created at: {dir_path}")


if __name__ == "__main__":
    main()
