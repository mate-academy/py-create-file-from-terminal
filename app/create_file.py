import sys
import os

from datetime import datetime


def create_directory(directory: str) -> None:
    os.makedirs(directory)


def create_file(file_creation: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_content = []

    line = input("Enter content line: ")
    while line != "stop":
        file_content.append(line)
        line = input("Enter content line: ")

    with open(file_creation, "w") as new_file:
        new_file.write(timestamp)
        for i, line in enumerate(file_content):
            new_file.write(f"{i + 1} {line}\n")


def main() -> None:
    line = sys.argv
    if "-d" in line:
        directory_index = line.index("-d") + 1
        directory_path = os.path.join(*line[directory_index:])
        create_directory(directory_path)

    elif "-f" in line:
        file_index = line.index("-f") + 1
        file_path = line[file_index]
        create_file(file_path)

    elif "-d" in line and "-f" in line:
        dir_index = line.index("-d") + 1
        file_index = line.index("-f") + 1
        directory_path = os.path.join(*line[dir_index:file_index - 1])
        file_name = line[file_index]
        file_path = os.path.join(directory_path, file_name)
        create_directory(directory_path)
        create_file(file_path)


if __name__ == "__main__":
    main()
