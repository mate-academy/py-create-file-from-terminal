import sys
import os

from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")


def get_content() -> str:
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {line}" for i, line in enumerate(lines)]
    return f"\n{timestamp}\n" + "\n".join(numbered_lines) + "\n"


def create_file(path: str, content: str) -> None:
    if os.path.exists(path):
        print(f"File '{path}' exists. Appending content.")
    else:
        print(f"Created the file '{path}'")
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    print("Content added successfully.")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d <dir_path> -f <file_name>")
        return

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path = os.path.join(*args[d_index + 1:f_index])
        else:
            dir_path = os.path.join(*args[d_index + 1:])
            create_directory(dir_path)
            return

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if file_name:
        full_path = os.path.join(dir_path, file_name)\
            if dir_path else file_name
        if dir_path:
            create_directory(dir_path)
        content = get_content()
        create_file(full_path, content)
    else:
        print("Error: No file name provided.")


if __name__ == "__main__":
    main()
