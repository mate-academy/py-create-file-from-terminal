import os
import sys
from datetime import datetime


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        interval = "\n"
    else:
        interval = ""
    with open(file_path, "a") as file:
        file.write(interval + get_timestamp() + "\n")
        print("Enter content line:")
        line_number = 1
        while True:
            line = input(f"{line_number} ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def create_directory(path_components: list) -> None:
    directory_path = os.path.join(*path_components)
    os.makedirs(directory_path, exist_ok=True)


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py "
              "-d <dir1> <dir2> ... -f <file_name>")
        sys.exit(1)

    if "-d" in sys.argv and "-f" not in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        create_directory(sys.argv[dir_index:])

    if "-f" in sys.argv and "-d" not in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        create_file(file_name)
    if "-f" in sys.argv and "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        file_path = sys.argv[dir_index:file_index - 1]
        full_path = os.path.join(*file_path, file_name)
        if not os.path.exists(os.path.join(*file_path)):
            create_directory(file_path)
            create_file(full_path)


if __name__ == "__main__":
    main()
