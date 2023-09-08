import os
import sys
import datetime


def create_file(file_path: str, content_lines: list) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(timestamp + "\n")
        for i, line in enumerate(content_lines, 1):
            file.write(f"{i} {line}\n")


def main() -> None:
    if len(sys.argv) < 3:
        print(
            "Usage: python create_file.py -d <directory_path> -f <file_name>"
        )
        sys.exit(1)

    if "-d" not in sys.argv or "-f" not in sys.argv:
        print("You must specify both -d and -f flags.")
        sys.exit(1)

    dir_index = sys.argv.index("-d")
    file_index = sys.argv.index("-f")

    if file_index - dir_index == 1:
        print("Directory path is missing.")
        sys.exit(1)

    directory_path = os.path.join(*sys.argv[dir_index + 1:file_index])
    file_name = sys.argv[file_index + 1]

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    file_path = os.path.join(directory_path, file_name)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            content = file.readlines()
        content_lines = [line.strip() for line in content[1:]]

    else:
        content_lines = []

    while True:
        line = input("Enter content line (or 'stop' to finish): ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    create_file(file_path, content_lines)
    print(f"File {file_path} created successfully.")
