from datetime import datetime
from os import makedirs, path
from sys import argv


def create_directories(directories: str) -> None:
    makedirs(directories, exist_ok=True)


def create_file_path() -> str:
    file_path = path.join(*argv[2:-2], argv[-1])
    return file_path


def file_input(file_path: str) -> None:
    with open(file_path, "a") as work_file:
        date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        work_file.write(date_time + "\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if "stop" == line.rstrip():
                work_file.write("\n")
                break
            work_file.write(f"{line_number} {line} \n")
            line_number += 1


if "-d" in argv and "-f" in argv:
    create_directories(path.join(*argv[2:-2]))
    file_input(create_file_path())
elif "-d" in argv:
    create_directories(path.join(*argv[2:]))
elif "-f" in argv:
    file_input(argv[-1])
