import sys
import os
from datetime import datetime


def create_path(directories_list: list) -> str:
    path = os.path.join(*directories_list)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_path: str) -> None:
    if not os.path.exists(file_path):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a") as file:
            file.write(f"{current_time}\n")

        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                with open(file_path, "a") as file:
                    file.write("\n")
                break
            with open(file_path, "a") as file:
                file.write(f"{line} {content}\n")
            line += 1
    else:
        print(f"File '{file_path}' already exists.")


def terminal() -> None:
    args = sys.argv[1:]

    directories = []
    file_path = None

    for i, arg in enumerate(args):
        if arg == "-d" and i + 1 < len(args):
            directories.append(args[i + 1])
        elif arg == "-f" and i + 1 < len(args):
            file_path = args[i + 1]

    if directories and file_path:
        path = create_path(directories)
        file_path = os.path.join(path, file_path)
        create_file(file_path)

    elif directories:
        create_path(directories)

    elif file_path:
        create_file(file_path)

    else:
        print("You should write correct request: "
              "python create_file.py "
              "(-d directory_path1 -d directory_path2 ...) "
              "(-f file_name)")


if __name__ == "__main__":
    terminal()
