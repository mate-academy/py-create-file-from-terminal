import sys
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    directories = []
    file_name = None

    if "-d" in args:
        index = args.index("-d") + 1
        while index < len(args) and args[index] != "-f":
            directories.append(args[index])
            index += 1

    if "-f" in args:
        index = args.index("-f") + 1
        if index < len(args):
            file_name = args[index]

    return directories, file_name


def create_directory_path(directories: list[str]) -> str:
    if not directories:
        return "."
    return os.path.join(*directories)


def ensure_directory_exists(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def collect_user_input() -> list[str]:
    print("Enter content line (type 'stop' to finish):")
    lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {text}" for i, text in enumerate(lines)]
    content = [timestamp] + numbered_lines

    needs_separator = (os.path.exists(file_path)
                       and os.path.getsize(file_path) > 0)

    with open(file_path, "a", encoding="utf-8") as source_file:
        if needs_separator:
            source_file.write("\n")
        source_file.write("\n".join(content) + "\n")

    print(f"File created or updated: {file_path}")


def main() -> None:
    directories, file_name = parse_arguments()
    directory_path = create_directory_path(directories)
    ensure_directory_exists(directory_path)

    if "-f" in sys.argv and not file_name:
        print("No file name provided with -f flag.")
        return
    if "-f" not in sys.argv:
        return
    file_path = os.path.join(directory_path, file_name)
    lines = collect_user_input()
    write_to_file(file_path, lines)


if __name__ == "__main__":
    main()
