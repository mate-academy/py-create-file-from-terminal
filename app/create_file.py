import os
import sys
from datetime import datetime


def create_directory(dirs: list) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_date}\n")
        line = 1

        while True:
            user_input = input("Write your content or enter 'stop' to exit: ")
            if user_input == "stop":
                break
            file.write(f"{line} Line{line} {user_input}" + "\n")
            line += 1
        file.write("\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        dir_index = args.index("-d")
        if "-f" in args:
            file_index = args.index("-f")
            dirs = args[dir_index + 1:file_index]
        else:
            dirs = args[dir_index + 1:]
        create_directory(dirs)

    if "-f" in args:
        file_index = args.index("-f")
        file_path = args[file_index + 1]
        create_file(file_path)


if __name__ == "__main__":
    main()
