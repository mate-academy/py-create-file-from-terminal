import os
import sys
from datetime import datetime


def create_dir(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully")

def get_content_from_user() -> list[str]:
    print("Enter content line (type 'stop' to finish):")
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines

def write_files(file_path: str, content_lines: list[str]) -> None:
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, line in enumerate(content_lines, 1):
            file.write(f"{i} {line}\n")

def main() -> None:
    args = sys.argv[1:]
    path = None
    file_name = None
    if "-d" in args:
        d_index = args.index("-d")
        path_parts = []
        for part in args[d_index + 1:]:
            if part.startswith("-"):
                break
            path_parts.append(part)
        if path_parts:
            path = os.path.join(*path_parts)
            create_dir(path)
        else:
            print("No directory path specified after -d.")
            sys.exit(1)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args) and not args[f_index + 1].startswith("-"):
            file_name = args[f_index + 1]
            # Перевіряємо, чи є створена директорія
            if path:
                file_path = os.path.join(path, file_name)
            else:
                file_path = file_name
        else:
            print("No file name specified after -f.")
            sys.exit(1)

    if file_name:
        content_lines = get_content_from_user()
        write_files(file_path, content_lines)
