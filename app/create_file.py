import os
import sys
from datetime import datetime


def create_file(directory: str, name: str) -> None:
    path_to_file = os.path.join(directory, name)

    with open(path_to_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line = 1
        while True:
            content = input("Enter content line:")
            if content.lower() == "stop":
                break

            file.write(f"{line} {content}\n")
            line += 1


def main() -> None:
    args = sys.argv[1:]

    dir_index = args.index("-d") if "-d" in args else None
    file_index = args.index("-f") if "-f" in args else None

    if dir_index is not None and file_index is not None:
        if file_index > dir_index:
            directory = os.path.join(*args[dir_index + 1:file_index])
            os.makedirs(directory, exist_ok=True)

            filename = args[file_index + 1]
            create_file(directory, filename)

        elif dir_index > file_index:
            directory = os.path.join(*args[file_index + 1:dir_index])
            os.makedirs(directory, exist_ok=True)

            filename = args[dir_index + 1]
            create_file(directory, filename)

    elif dir_index is not None:
        directory = os.path.join(*args[dir_index + 1:])
        os.makedirs(directory, exist_ok=True)

    elif file_index is not None:
        create_file(os.getcwd(), args[file_index + 1])


if __name__ == "__main__":
    main()
