from datetime import datetime
import sys
import os

command = sys.argv


def create_directory() -> None:
    index_d = command.index("-d") if "-d" in command else None
    index_f = command.index("-f") if "-f" in command else None

    if index_d is not None:
        if index_f is not None and index_f > index_d:
            directory = os.path.join(
                os.getcwd(), *command[index_d + 1:index_f]
            )
            os.makedirs(directory, exist_ok=True)
            create_file(directory, command[index_f + 1])
        elif index_f is not None and index_f < index_d:
            directory = os.path.join(
                os.getcwd(), *command[index_d + 1:]
            )
            os.makedirs(directory, exist_ok=True)
            create_file(directory, command[index_f + 1])
        else:
            directory = os.path.join(
                os.getcwd(), *command[index_d + 1:]
            )
            os.makedirs(directory, exist_ok=True)
    elif "-f" is not None:
        create_file(os.getcwd(), command[index_f + 1])


def create_file(directory: str, filename: str) -> None:
    file_path = os.path.join(directory, filename)
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
