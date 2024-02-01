import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created.")
    else:
        print(f"Directory {path} already exists.")


def write_to_file(file_path: str, content: list) -> None:
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")
        directory = os.path.join(*sys.argv[dir_index + 1:file_index])
        file_name = sys.argv[file_index + 1]
        create_directory(directory)
        file_path = os.path.join(directory, file_name)
    elif "-d" in sys.argv:
        directory = os.path.join(*sys.argv[2:])
        create_directory(directory)
        return
    elif "-f" in sys.argv:
        file_path = sys.argv[sys.argv.index("-f") + 1]
    else:
        print("Invalid arguments")
        return

    content = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)

    write_to_file(file_path, content)


if __name__ == "__main__":
    main()
