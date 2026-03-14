import os
import sys
from datetime import datetime


def get_user_lines() -> list:
    lines = []
    print(
        "Enter content line (type 'stop' to finish):"
    )
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as target_file:
        if mode == "a":
            target_file.write("\n")

        target_file.write(f"{timestamp}\n")
        for line_number, content in enumerate(lines, 1):
            target_file.write(f"{line_number} {content}\n")


def main() -> None:
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
            if i < len(args) and not args[i].startswith("-"):
                file_name = args[i]
                i += 1
            else:
                print("Error: -f requires a valid filename.")
                sys.exit(1)
        else:
            i += 1

    target_path = os.path.join(*directory_parts) if directory_parts else "."

    if directory_parts:
        os.makedirs(target_path, exist_ok=True)

    if file_name:
        full_file_path = os.path.join(target_path, file_name)
        lines = get_user_lines()
        write_to_file(full_file_path, lines)


if __name__ == "__main__":
    main()
