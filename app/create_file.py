import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv
    dir_index = -1
    file_index = -1
    directory_path = ""
    file_name = ""

    if "-d" in args:
        dir_index = args.index("-d")
        directory_path = os.path.join(*args[dir_index + 1:])

    if "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]

    if dir_index != -1 and file_index != -1 and dir_index < file_index:
        directory_path = os.path.join(*args[dir_index + 1:file_index])
        os.makedirs(directory_path, exist_ok=True)
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)

    elif dir_index != -1:
        os.makedirs(directory_path, exist_ok=True)

    elif file_index != -1:
        create_file(file_name)


def create_file(file_name: str) -> None:
    directory_path = os.getcwd()
    mode = "a" if os.path.exists(file_name) else "w"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(directory_path, file_name), mode) as file:
        file.write(timestamp + "\n")
        num = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                file.write(" \n")
                break
            file.write(f"{str(num)} {content} \n")
            num += 1


if __name__ == "__main__":
    main()
