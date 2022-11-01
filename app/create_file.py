import os
from datetime import datetime


def flags_choice() -> None:
    enter_flag = input("Enter flags: ")

    while True:
        if "-d" == enter_flag.strip():
            create_directory()
        if "-f" == enter_flag.strip():
            create_file()
        if "-d -f" == enter_flag.strip():
            create_directory()
            create_file()
        else:
            break


def time_stamp() -> str:
    now = datetime.now()
    now_time = now.strftime(f"{datetime.date(now)} {'%H:%M:%S'}")
    return now_time


def create_directory() -> None:

    while True:
        name_directory = input("Enter name directory: ")

        if name_directory.strip() == "stop":
            break
        try:
            os.makedirs(name_directory)
            os.chdir(f"{name_directory}/")
        except FileExistsError:
            print(f"File exists: {name_directory}")


def create_file() -> None:
    count_lines = 1
    file_name = input("Enter file_name: ")

    with open(f"{file_name}.txt", "a") as file_create:
        file_create.write(f"\n{time_stamp()}\n")
    while True:
        content_file = input("Enter content line: ")
        if content_file.strip() == "stop":
            break
        with open(f"{file_name}.txt", "a+") as file:
            file.write(f"{count_lines} {content_file}\n")
            count_lines += 1


flags_choice()
