import os
import sys
from datetime import datetime


def write_content(file_path: str) -> None:
    content = []
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        for line_number, line_content in enumerate(content, 1):
            file.write(f"{line_number} {line_content}\n")
        file.write("\n")


def create_file(file_name: str) -> None:
    mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, mode):
        write_content(file_name)


def create_file_with_directory(directory_path: str, file_name: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)
    file_path = os.path.join(directory_path, file_name)
    create_file(file_path)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py"
              " [-d directory_path] [-f file_name]")
        return

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        if d_index < f_index:
            directory_path = os.path.join(*args[d_index + 1:f_index])
        else:
            directory_path = os.path.join(*args[d_index + 1:])
        file_name = args[f_index + 1]
        create_file_with_directory(directory_path, file_name)
    elif "-d" in args:
        directory_index = args.index("-d") + 1
        directory_path = os.path.join(*args[directory_index:])
        os.makedirs(directory_path, exist_ok=True)
    elif "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        create_file(file_name)


if __name__ == "__main__":
    main()
