import os
from datetime import datetime
from typing import List


def create_directory(dir_name: str) -> None:
    if dir_name:
        path = os.path.join(*dir_name)
        os.makedirs(path, exist_ok=True)
        os.chdir(path)


def write_content_to_file(file_name: str, content: List[str]) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now():%Y-%m-%d %H:%M:%S\n}")
        index = 1
        for line in content:
            if line != "\n":
                file.write(f"{index} {line}\n")
                index += 1
            else:
                file.write("\n")


def main() -> None:
    command = input()

    if "-f" in command:
        file_index = command.index("-f")
        file_name = command[file_index + 1]
    else:
        file_name = None

    if "-d" in command:
        dir_index = command.index("-d")
        dir_name = command[dir_index + 1:]
    else:
        dir_name = None

    content = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            content.append("\n")
            break
        content.append(content_line)

    create_directory(dir_name)
    write_content_to_file(file_name, content)


if __name__ == "__main__":
    main()
