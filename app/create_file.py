import sys
import os
from datetime import datetime


def create_directory(path_parts: list[str]) -> None:
    if not os.path.exists(os.path.join(*path_parts)):
        os.makedirs(os.path.join(*path_parts))
        print(f"Directory '{os.path.join(*path_parts)}' created!")

    else:
        print(f"Directory '{os.path.join(*path_parts)}' already exists.")


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"File '{file_path}' exists. Appending new content...")
    else:
        print(f"Creating new file: '{file_path}'")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        f.write(f"\n{timestamp}\n")

        str_count = 1
        while True:
            content = input(f"Enter content line {str_count}: ")
            if content.lower() == "stop":
                break
                f.write(f"{str_count} {content}\n")
                str_count += 1

        if __name__ == "__main__":
            if len(sys.argv) < 2:
                print("Arguments Error!")
                sys.exit(1)

    if "-d" in sys.argv:
        dir_parts = sys.argv[sys.argv.index("-d") + 1:]
        if "-f" in dir_parts:
            dir_parts = dir_parts[:dir_parts.index("-f")]
        create_directory(dir_parts)

    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        if "-d" in sys.argv:
            directory_path = (os.path.join
                              (*sys.argv[sys.argv.index("-d")
                                         + 1:sys.argv.index("-f")]))
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        create_file(file_path)
