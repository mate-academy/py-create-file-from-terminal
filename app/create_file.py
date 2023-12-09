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
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        if file_index > dir_index:
            directory = os.path.join(*args[dir_index + 1:file_index])
            os.makedirs(directory, exist_ok=True)

            filename = args[file_index + 1]
            create_file(directory, filename)
    elif "-d" in args:
        dir_index = args.index("-d")
        directory = os.path.join(*args[dir_index + 1:])
        os.makedirs(directory, exist_ok=True)

    elif "-f" in args:
        file_index = args.index("-f")
        create_file(os.getcwd(), args[file_index + 1])


if __name__ == "__main__":
    main()
