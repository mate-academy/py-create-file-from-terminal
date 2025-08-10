import sys
import os
from datetime import datetime


def create_and_write_file(file_path_or_name: str) -> None:
    with open(file_path_or_name, "a") as new_file:
        now = datetime.now()
        new_file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        number_line = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                break
            new_file.write(f"{number_line} {content_line}\n")
            number_line += 1

        new_file.write("\n")


def create_directory(path_of_directories: str) -> None:
    os.makedirs(path_of_directories, exist_ok=True)


if "-d" in sys.argv and "-f" in sys.argv:
    directory_path_list = sys.argv[sys.argv.index("-d") + 1:
                                   sys.argv.index("-f")]
    file_name = sys.argv[sys.argv.index("-f") + 1:][0]

    path = os.path.join(*directory_path_list)
    create_directory(path)

    file_path = os.path.join(path, file_name)
    create_and_write_file(file_path)
elif "-d" in sys.argv:
    directory_path_list = sys.argv[sys.argv.index("-d") + 1:]
    create_directory(os.path.join(*directory_path_list))
elif "-f" in sys.argv:
    file_name = sys.argv[sys.argv.index("-f") + 1:][0]
    create_and_write_file(file_name)
