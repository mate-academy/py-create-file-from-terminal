import sys
import os
from datetime import datetime


def create_directory(path_parts: str) -> None:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory created: {directory_path}")


def create_file(file_name: str, directory_path: str = None) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if directory_path:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = os.path.join(os.getcwd(), file_name)
    content_lines = []

    print("Enter content line (input 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_path, "a") as file:
        file.write(timestamp + "\n")
        for line_number, line in enumerate(content_lines, start=1):
            file.write(f"{line_number} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" not in args:
        dir_index = args.index("-d") + 1
        dir_parts = args[dir_index:]
        create_directory(dir_parts)

    elif "-f" in args and "-d" not in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        create_file(file_name)

    else:
        dir_index = args.index("-d") + 1
        dir_parts = args[dir_index:args.index("-f")]
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        create_directory(dir_parts)
        directory_path = os.path.join(os.getcwd(), *dir_parts)
        create_file(file_name, directory_path)


if __name__ == "__main__":
    main()
