import os
import argparse
from datetime import datetime


def create_directory(path_parts: list) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_path, "a") as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f", required=True)
    args = parser.parse_args()

    full_dir = create_directory(args.d) if args.d else os.getcwd()
    file_path = os.path.join(full_dir, args.f)
    write_to_file(file_path)


if __name__ == "__main__":
    main()
