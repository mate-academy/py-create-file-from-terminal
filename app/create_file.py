import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
        )
        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{line} {content} \n")
            line += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        _, command_d, *directories, command_f, file_name = sys.argv
        path = create_path(directories)
        create_file(f"{path}/{file_name}")
        return

    if "-d" in sys.argv:
        _, command_d, *directories = sys.argv
        create_path(directories)
        return

    if "-f" in sys.argv:
        create_file(sys.argv[-1])
        return


if __name__ == "__main__":
    main()
