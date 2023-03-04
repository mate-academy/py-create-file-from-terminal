import datetime
import os
import sys


def file_from_terminal() -> None:
    directory = sys.argv
    if "-d" in directory and "-f" in directory:
        check_variable = " ".join(directory)
        if check_variable.index("-d") < check_variable.index("-f"):
            os.chdir(create_directory(directory[2:-2]))
            create_file(directory[-1])
            return
        else:
            create_directory(directory[directory.index("-d") + 1::])
            create_file(directory[directory.index("-f") + 1])
            return
    if "-d" in directory:
        create_directory(directory[2:])

    if "-f" in directory:
        create_file(directory[2])


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.datetime.now().strftime(
            "%y-%m-%d %H:%M:%S\n"))
        count = 0
        while True:
            count += 1
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{count} {text}\n")


def create_directory(directories: list) -> str:
    path_to_directory = os.path.join(*directories)
    os.makedirs(path_to_directory, exist_ok=True)
    return path_to_directory


if __name__ == "__main__":
    file_from_terminal()
