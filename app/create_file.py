import os
import sys
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    dir_path = []
    file_name = ""

    if "-d" in args:
        try:
            start_index = args.index("-d") + 1
            end_index = args.index("-f") if "-f" in args else len(args)
            dir_path = args[start_index:end_index]
            if not dir_path:
                raise ValueError("Directory path not specified after '-d'.")
        except ValueError:
            raise ValueError("Incorrect usage of '-d' flag.")

    if "-f" in args:
        try:
            file_index = args.index("-f") + 1
            file_name = args[file_index]
            if file_name.startswith("-"):
                raise ValueError("File name not specified after '-f'.")
        except IndexError:
            raise ValueError("File name not specified after '-f'.")

    if "-d" not in args and "-f" not in args:
        raise ValueError("Neither '-d' nor '-f' flags were provided.")

    return dir_path, file_name


def create_directory(dir_path: list) -> str:
    if dir_path:
        full_dir_path = os.path.join(*dir_path)
        try:
            os.makedirs(full_dir_path, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory: {e}")
            sys.exit(1)
        return full_dir_path
    return ""


def collect_content_lines() -> list:
    print("Enter content line (type 'stop' to finish):")
    content_lines = []
    count = 1
    while True:
        line = input()
        if line == "stop":
            break
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content_lines.append(f"{timestamp} - {count}. {line}\n")
        count += 1
    return content_lines


def write_content_to_file(full_path: str, content_lines: list) -> None:
    try:
        with open(full_path, "a") as f:
            if os.path.getsize(full_path) > 0:
                f.write("\n")
            f.writelines(content_lines)
    except IOError as e:
        print(f"Error writing to file: {e}")


def main() -> None:
    args = sys.argv[1:]
    dir_path, file_name = parse_arguments(args)
    full_dir_path = create_directory(dir_path)
    full_path = os.path.join(full_dir_path, file_name)\
        if full_dir_path else file_name
    if not file_name:
        sys.exit(1)
    write_content_to_file(full_path, collect_content_lines())


if __name__ == "__main__":
    main()
