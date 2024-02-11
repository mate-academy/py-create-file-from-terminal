import sys
import os
from datetime import datetime


def create_directory_if_not_exists(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def get_content_from_user() -> list:
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)
    return content


def write_content_to_file(file_path: str, content: list) -> None:
    with open(file_path, "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for number, line in enumerate(content):
            f.write(f"{number} {line}\n")


def main() -> None:
    command = sys.argv

    if "-d" in command:
        directory_index = command.index("-d") + 1
        if "-f" in command:
            file_index = command.index("-f")
            directory_path = os.path.join(
                *command[directory_index:file_index - 1]
            )
            create_directory_if_not_exists(directory_path)
            os.chdir(directory_path)
        else:
            directory_path = os.path.join(*command[directory_index:])
            create_directory_if_not_exists(directory_path)

    if "-f" in command:
        file_path = command[-1]
        content = get_content_from_user()
        write_content_to_file(file_path, content)


if __name__ == "__main__":
    main()
