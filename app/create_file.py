from datetime import datetime
import sys
import os

command = sys.argv


def create_directory() -> None:
    if "-d" in command:
        index_d = command.index("-d") + 1
        if "-f" in command:
            index_f = command.index("-f") + 1
            directory = (
                os.path.join(os.getcwd(), *command[index_d:index_f - 1])
            )
            make_dir(directory)
            create_file(directory, index_f)
        if "-f" not in command:
            directory = os.path.join(os.getcwd(), *command[index_d:])
            make_dir(directory)
    if "-f" in command:
        index_f = command.index("-f") + 1
        create_file(os.getcwd(), index_f)


def make_dir(directory: str) -> None:
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass


def create_file(directory: str, index: int) -> None:
    file_path = os.path.join(directory, command[index])
    with open(file_path, "a") as source_file:
        line_count = 0
        date_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{date_time}\n")
        while True:
            content = input("Enter content line: ")
            line_count += 1
            if content == "stop":
                break
            source_file.write(f"{line_count} {content}\n")


create_directory()
