import os
import sys
from datetime import datetime


def create_directories(path_parts: list) -> list:
    directory_path = os.path.join(*path_parts)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    return directory_path


def write_content_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        f.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        directories = args[d_index + 1:]

        if "-f" in directories:
            f_index = directories.index("-f")
            file_name = directories[f_index + 1]
            directories = directories[:f_index]
            create_directories(directories)
            write_content_to_file(os.path.join(*directories, file_name))
        else:
            create_directories(directories)

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        write_content_to_file(file_name)


if __name__ == "__main__":
    main()
