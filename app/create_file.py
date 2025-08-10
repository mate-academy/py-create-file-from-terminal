import os
import sys
from datetime import datetime


def create_directory(dir_path: str) -> str:
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = []

    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(content, start=1):
            file.write(f"{index} {line}\n")
        file.write("\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        dir_path = os.path.join(*args[d_index + 1:f_index])
        create_directory(dir_path)

        file_name = args[f_index + 1]
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)

    elif "-d" in args:
        d_index = args.index("-d")
        dir_path = os.path.join(*args[d_index + 1:])
        create_directory(dir_path)
        print(f"Directory created: {dir_path}")

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)
        print(f"File created/updated: {file_name}")

    else:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f file_name]")


if __name__ == "__main__":
    main()
