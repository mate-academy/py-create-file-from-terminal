import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def add_content(file_to_write: str) -> None:
    with open(file_to_write, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line = 1

        while (data := input("Enter content line: ")) != "stop":
            file.write(f"{line} {data}" + "\n")
            line += 1


def write_file(path_file: str) -> None:
    if not os.path.exists(path_file):
        with open(path_file, "w"):
            add_content(path_file)
            return

    with open(path_file, "a") as f:
        f.write("\n")


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        _, command_d, *directories, command_f, file_name = sys.argv
        path = create_path(directories)
        write_file(f"{path}/{sys.argv[-1]}")
        return

    if "-d" in sys.argv:
        _, command_d, *directories = sys.argv
        create_path(directories)
        return

    if "-f" in sys.argv:
        write_file(sys.argv[-1])
        return


if __name__ == "__main__":
    main()
