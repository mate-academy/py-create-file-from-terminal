import os
import sys
from datetime import datetime


timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_path(directories: list[str]) -> str:
    path = os.path.join(*directories)
    return path


def create_directory(directory_path: str) -> None:
    try:
        os.makedirs(directory_path)
    except OSError:
        print("Directory exists already!")


def create_file(file_name: str) -> None:

    with open(file_name, "a") as file:

        file.write(f"{timestamp} \n")
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_num} {line} \n")
            line_num += 1


def main() -> None:

    if "-d" in sys.argv and "-f" not in sys.argv:
        dir_index = sys.argv.index("-d")
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        create_directory(directory_path)

    if "-f" in sys.argv and "-d" not in sys.argv:
        file_index = sys.argv.index("-f")
        file_name = sys.argv[file_index + 1]
        create_file(file_name)

    if "-f" in sys.argv and "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")
        file_path = create_path(sys.argv[dir_index + 1:file_index])
        create_directory(file_path)
        path_to_file = file_path + "/" + sys.argv[-1]
        create_file(path_to_file)


if __name__ == "__main__":
    main()
