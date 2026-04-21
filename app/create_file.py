import datetime
import os
import sys


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_dir(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as source_file:
        source_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                          + "\n")
        i = 1

        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            source_file.write(f"{i} {content_line}\n")
            i += 1


def create_file_from_terminal() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_path = create_path(sys.argv[2:-2])
        file_path = os.path.join(dir_path, sys.argv[-1])
        create_dir(dir_path)
        create_file(file_path)

    elif "-d" in sys.argv:
        create_dir(create_path(sys.argv[2:-2]))

    elif "-f" in sys.argv:
        create_file(sys.argv[-1])


create_file_from_terminal()
