import os
import sys
from datetime import datetime
from typing import List


def create_file(directory: str, filename: str, content: List[str]) -> None:
    file_path = os.path.join(directory, filename)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n\n")
            file.write(timestamp + "\n")
            for line in content:
                file.write(line + "\n")
    else:
        with open(file_path, "w") as file:
            file.write(timestamp + "\n")
            for line in content:
                file.write(line + "\n")

    print(f"File '{filename}' created successfully at '{file_path}'.")


def process_arguments(args: List[str]) -> None:
    if "-d" in args:
        directory_index = args.index("-d") + 1
        path = [*args[directory_index:]]
        if "-f" in path:
            p_index = path.index("-f")
            path = path[:p_index]
            directory_path = os.path.join(*path)
        else:
            directory_path = os.path.join(*args[directory_index:])
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = "."

    if "-f" in args:
        filename_index = args.index("-f") + 1
        filename = args[filename_index]
        content = get_content_from_input()
        create_file(directory_path, filename, content)


def get_content_from_input() -> List[str]:
    content = []
    line = input("Enter content line: ")
    while line != "stop":
        content.append(line)
        line = input("Enter content line: ")
    return content


if __name__ == "__main__":
    arguments = sys.argv[1:]
    process_arguments(arguments)
