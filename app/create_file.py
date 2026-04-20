import sys
import os
from datetime import datetime


def create_directory(path):
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path):
    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {line}" for i, line in enumerate(content_lines)]
    content = f"\n{timestamp}\n" + "\n".join(numbered_lines) + "\n"

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode, encoding="utf-8") as file:
        file.write(content)

    print(f"File created/updated: {file_path}")


def main():
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else None

        if f_index:
            dir_path = os.path.join(*args[d_index + 1:f_index])
            file_name = args[f_index + 1]
            create_directory(dir_path)
            file_path = os.path.join(dir_path, file_name)
            create_file(file_path)
        else:
            dir_path = os.path.join(*args[d_index + 1:])
            create_directory(dir_path)
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)
    else:
        print("Usage: python create_file.py -d [directory_path] -f [file_name]")


if __name__ == "__main__":
    main()
