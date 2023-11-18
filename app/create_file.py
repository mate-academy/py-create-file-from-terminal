import os
import sys

from datetime import datetime


def create_file(
        directory: list[str],
        file_name: str,
        file_content: str
) -> None:

    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        path = os.path.join(directory_path, file_name)
    else:
        path = file_name

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "a") as f:
        f.write(timestamp + "\n")
        for i, line in enumerate(file_content.splitlines(), 1):
            f.write(f"{i} {line}\n")


def main() -> None:
    directory_path = None
    file_name = None

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory_path = sys.argv[dir_index:]
        if "-f" not in sys.argv:
            os.makedirs(os.path.join(*directory_path), exist_ok=True)
            return

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]

    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_name = sys.argv.index("-f") + 1

        if dir_index < file_name:
            directory_path = sys.argv[dir_index:file_name - 1]
        else:
            directory_path = sys.argv[dir_index:]

    file_content = ""

    while 1:
        line = input("Enter content line: ")
        if line == "stop":
            break

        file_content += line + "\n"

    create_file(directory_path, file_name, file_content)


if __name__ == "__main__":
    main()
