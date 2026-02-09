import sys
import os
from datetime import datetime


def create_content() -> list:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    content = []
    content.append(timestamp)

    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(f"{line_number} {line}")
        line_number += 1

    return content


def create_file(file_path: str, content: list) -> None:
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        file.write("\n")
        for entry in content:
            file.write(entry + "\n")


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py "
              "[-d directory_path] [-f file_name]")
        return

    dir_path = ""
    file_name = ""

    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        dir_path = os.path.join(*sys.argv[dir_index: file_index - 1])
        file_name = sys.argv[file_index]
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dir_path = os.path.join(*sys.argv[dir_index:])
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]

    if dir_path:
        create_directory(dir_path)
    if file_name:
        file_path = os.path.join(dir_path, file_name)
        content = create_content()
        create_file(file_path, content)


if __name__ == "__main__":
    main()
