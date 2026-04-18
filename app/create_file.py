import sys
import os
from datetime import datetime


def create_file_app() -> None:
    args = sys.argv[1:]
    valid_flags = ["-d", "-f"]
    if not args:
        print("Error: No arguments provided.")
        return

    if args[0] not in valid_flags:
        print(f"Error: The first argument must be a valid flag: {valid_flags}")
        return

    path_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                path_parts.append(args[i])
                i += 1
            continue
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            continue
        i += 1

    target_dir = os.path.join(*path_parts) if path_parts else "."

    if path_parts:
        os.makedirs(target_dir, exist_ok=True)

    if not file_name:
        abs_path = os.path.abspath(target_dir)
        print(f"Directories were created at: {abs_path}")
        return

    full_path = os.path.join(target_dir, file_name)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n")
        for idx, content in enumerate(lines, 1):
            f.write(f"{idx} {content}\n")

if __name__ == "__main__":
    create_file_app()
