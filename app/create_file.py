from datetime import datetime
from os import makedirs, path
from sys import argv


def create_directories(directories: str) -> None:
    makedirs(directories, exist_ok=True)


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


def flags_passed() -> None:
    if "-d" in argv and "-f" in argv:
        if argv.index("-d") < argv.index("-f"):
            create_directories(path.join(*argv[2:-2]))
            file_input(path.join(*argv[2:-2], argv[-1]))
        else:
            create_directories(path.join(*argv[4:]))
            file_input(path.join(*argv[4:], argv[2]))
    elif "-d" in argv:
        create_directories(path.join(*argv[2:]))
    elif "-f" in argv:
        file_input(argv[-1])


if __name__ == "__main__":
    flags_passed()
