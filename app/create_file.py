import sys
import os
from datetime import datetime


def create_directory(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")


def get_file_content() -> list[str]:
    print("Enter content line (type 'stop' to finish):")
    content_line = []
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_line.append(f"{line_number} {line}")
        line_number += 1
    return content_line


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"\n{timestamp}\n" + "\n".join(content_lines) + "\n"
    try:
        with open(file_path, "a") as file:
            file.write(content)
        print(f"Content added to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")


def main() -> None:
    args = sys.argv[1:]
    try:
        if not args or ("-d" not in args and "-f" not in args):
            print("Usage: python create_file.py -d "
                  "[directory path] -f [filename]")
            return
    except Exception as e:
        print(f"Error parsing arguments. "
              f"check the correctness of the arguments (-f) (-d): {e}")
        return

    directory = ""
    filename = ""

    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else len(args)
        directory = os.path.join(*args[d_index + 1:f_index])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]
        else:
            print("Error: No filename provided after '-f'")
            return

    if directory:
        create_directory(directory)

    if filename:
        file_path = os.path.join(directory, filename) \
            if directory else filename
        content_lines = get_file_content()
        write_to_file(file_path, content_lines)
