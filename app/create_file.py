import os
import sys
from datetime import datetime


def make_directories(args: list) -> str | bytes:
    dir_path = os.path.join(*args)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory {dir_path} created.")
    return dir_path


def create_file_with_content(file_path: str) -> None:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_content = f"{timestamp}\n"
    new_content += "\n".join([f"{i + 1} {line}" for i, line in enumerate(content_lines)])

    mode = 'a' if os.path.exists(file_path) else 'w'
    with open(file_path, mode) as file:
        if mode == 'a':
            file.write("\n\n")
        file.write(new_content)
    print(f"File {file_path} created with content.")


def main() -> None:
    args = sys.argv
    if "-d" in args and "-f" in args:
        path = make_directories(args[2:-2])
        create_file_with_content(os.path.join(path, args[-1]))
    elif "-d" in args:
        make_directories(args[2:])
    elif "-f" in args:
        create_file_with_content(args[-1])


if __name__ == "__main__":
    main()
