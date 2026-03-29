import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    try:
        os.makedirs(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_or_append_file(file_path: str) -> None:
    try:
        with open(file_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n{timestamp}\n")

            line = 1
            while True:
                content = input("Enter content line: ")
                if content.lower() == "stop":
                    break
                file.write(f"{line} {content}\n")
                line += 1
    except PermissionError:
        print(f"Permission denied: Unable to create '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_file() -> None:
    args = sys.argv[1:]
    if "-d" not in args or "-f" not in args:
        print("You should provide -f or -d flag")
        return

    directory_paths = []
    file_name = None
    if "-d" in args:
        dir_idx = args.index("-d")
        for arg in args[dir_idx + 1:]:
            if arg == "-f":
                break
            directory_paths.append(arg)

    if "-f" in args:
        file_idx = args.index("-f")
        file_name = args[file_idx + 1]

    if directory_paths:
        dir_path = os.path.join(*directory_paths)
        create_directory(dir_path)
    if file_name:
        file_path = os.path.join(dir_path, file_name)
        create_or_append_file(file_path)


if __name__ == "__main__":
    create_file()
