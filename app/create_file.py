import os
import sys
from datetime import datetime


def create_file(file_path: str) -> None:
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.insert(0, timestamp)

    with open(file_path, "a") as file:
        file.write("\n".join(content))


def main() -> None:
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory_path = os.path.join(*sys.argv[dir_index:])
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = os.getcwd()

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
