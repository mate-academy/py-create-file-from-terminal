import os
import sys
from datetime import datetime


def create_dir(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except FileExistsError:
        print(f"Directory {path} already exist")


def create_file(file_path: str) -> None:
    try:
        with open(file_path, "w") as file:
            print(f"Created file: {file_path}")
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            while True:
                content_line = input("Enter content line:")
                if content_line.lower() == "stop":
                    break
                file.write(content_line)
    except FileExistsError:
        print(f"File {file_path} already exist")


def main() -> None:
    if sys.argv[1] == "-d":
        directory_path = os.path.join(*sys.argv[2:])
        create_dir(directory_path)
    elif sys.argv[1] == "-f":
        file_name = sys.argv[2]
        create_file(file_name)
    else:
        print("Usage: python create_file.py "
              "[-d <directory_path>] [-f <file_name>]")
    sys.exit(1)


if __name__ == "__main__:":
    main()
