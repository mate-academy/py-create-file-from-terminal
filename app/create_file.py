import os
import sys
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    try:
        dir_path = args[args.index("-d") + 1:args.index("-f")]
    except ValueError:
        dir_path = args[args.index("-d") + 1:] if "-d" in args else []
    try:
        file_name = args[args.index("-f") + 1]
    except (ValueError, IndexError):
        file_name = ""
    return dir_path, file_name


def create_directory(dir_path: list) -> str:
    if dir_path:
        full_dir_path = os.path.join(*dir_path)
        os.makedirs(full_dir_path, exist_ok=True)
        return full_dir_path
    return ""


def collect_content_lines() -> list:
    print("Enter content line (type 'stop' to finish):")
    content_lines = []
    while True:
        line = input()
        if line == 'stop':
            break
        content_lines.append(line)
    return content_lines


def write_content_to_file(full_path: str, content_lines: list) -> None:
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = [f"{timestamp}\n"] + [f"{i + 1}. {line}\n" for i, line in enumerate(content_lines)]
        with open(full_path, "a") as f:
            if os.path.getsize(full_path) > 0:
                f.write("\n")
            f.writelines(content)
    except IOError as e:
        print(f"Error writing to file: {e}")


def main() -> None:
    args = sys.argv[1:]
    dir_path, file_name = parse_arguments(args)

    if not file_name:
        print("Error: No file name provided.")
        sys.exit(1)

    full_dir_path = create_directory(dir_path)
    full_path = os.path.join(full_dir_path, file_name) if full_dir_path else file_name
    content_lines = collect_content_lines()
    write_content_to_file(full_path, content_lines)


if __name__ == "__main__":
    main()
