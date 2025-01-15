import sys
import os
from datetime import datetime


def create_directory(path_parts: str) -> any:
    directory = os.path.join(*path_parts)
    os.makedirs(directory, exist_ok=True)
    print(f"Directory created: {directory}")
    return directory


def create_file(file_path: str) -> any:
    lines = []
    print("Enter content lines (type 'stop' to finish):")

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"\n{timestamp}\n"
    content += "\n".join(f"{i + 1} {line}" for i, line in enumerate(lines))

    if os.path.exists(file_path):
        print(f"File already exists. Appending content to {file_path}")
        mode = "a"
    else:
        print(f"Creating file: {file_path}")
        mode = "w"

    with open(file_path, mode) as file:
        file.write(content + "\n")

    print(f"Content written to {file_path}")


def main() -> any:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [dir ...] -f [file]")
        return

    directory_parts = []
    file_name = None
    flag = None

    for arg in args:
        if arg == "-d":
            flag = "directory"
        elif arg == "-f":
            flag = "file"
        else:
            if flag == "directory":
                directory_parts.append(arg)
            elif flag == "file" and not file_name:
                file_name = arg
            else:
                print(f"Unexpected argument: {arg}")
                return

    if not directory_parts and not file_name:
        print("Error: No valid directory or file specified.")
        return

    current_path = os.getcwd()

    if directory_parts:
        directory_path = create_directory(directory_parts)
    else:
        directory_path = current_path

    if file_name:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
