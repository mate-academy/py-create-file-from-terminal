import os
import datetime
import sys


def create_path_directory(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def create_and_writing_to_file(file_name: str) -> None:
    page_number = 1
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, "a") as source_file:
            source_file.write("\n")

    while True:
        message = input("Enter content line: ")
        if message == "stop":
            break
        with open(file_name, "a") as source_file:
            if page_number == 1:
                source_file.write(f"{date}\n")
            source_file.write(f"{page_number} {message}\n")
        page_number += 1
    page_number = 0


terminal_path = sys.argv

if "-f" not in terminal_path:
    directories = terminal_path[2:]
    create_path_directory(directories)
elif "-d" not in terminal_path:
    file_name = terminal_path[2]
    create_and_writing_to_file(file_name)
else:
    directories = terminal_path[2:-2]
    file_name = terminal_path[-1:]
    path_to_file = str(os.path.join(*directories, *file_name))

    create_path_directory(directories)
    create_and_writing_to_file(path_to_file)
