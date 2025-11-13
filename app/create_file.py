import datetime
import sys
import os


command = sys.argv


def create_path(command: list) -> None:
    path = None

    if "-d" in command:
        index_d = command.index("-d")
        if "-f" in command:
            index_f = command.index("-f")
            dirs = command[index_d + 1:index_f]
        else:
            dirs = command[index_d + 1:]
        path = os.path.join(*dirs)
    return path


def create_file(command: list) -> None:
    path = None
    file_name = "new_file.txt"

    if "-d" in command:
        path = create_path(command)
        os.makedirs(path, exist_ok=True)

    if "-f" in command:
        index_f = command.index("-f")
        file_name = command[index_f + 1]

    if path:
        full_path = os.path.join(path, file_name)
    else:
        full_path = file_name

    is_active = True

    counter = 1

    with open(full_path, "a") as new_file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(f"{time_now}\n\n")
        while is_active:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            new_file.write(f"{counter} {line}\n")
            counter += 1
