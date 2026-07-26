from datetime import datetime
import os
import sys


def created_directories(path_parts: list[str]) -> any:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(filepath: str) -> None:
    lines = []
    while True:
        line = input("Enter new line of content:")
        if line.lower() == "stop":
            break
        lines.append(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a") as file:
        file.write(f"{timestamp}\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return
    dir_parts = []
    filename = None
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
                filename = args[i]
                i += 1
            else:
                print("Error: filename not provided after -f")
                return
        else:
            i += 1

    directory = created_directories(dir_parts) if dir_parts else "."

    if filename:
        filepath = os.path.join(directory, filename)
        write_to_file(filepath)
        print(f"File saved to: {filepath}")
    else:
        print("No file name provided. Use -f <filename>")


if __name__ == "__main__":
    main()
