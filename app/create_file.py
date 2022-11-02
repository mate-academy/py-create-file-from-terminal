import os
import sys
from datetime import datetime


def flags_choice() -> None:
    user_input = sys.argv

    if "-d" in user_input and "-f" in user_input:
        create_directory(user_input[2:4])
        create_file(user_input[-1])
        sys.exit("EXIT")

    if "-d" in user_input:
        create_directory(user_input[2:])

    if "-f" in user_input:
        create_file(user_input[2])


def time_stamp() -> str:
    now = datetime.now()
    now_time = now.strftime(f"{datetime.date(now)} {'%H:%M:%S'}\n")
    return now_time


def create_directory(folders: list) -> None:
    try:
        for folder in folders:
            os.mkdir(folder)
            os.chdir(folder)
    except FileExistsError:
        print(f"File {folder} exists in this directory")


def create_content(new_file: [object]) -> None:
    count_lines = 1
    while True:
        content = input("Enter content line: ")
        if content.lower().strip() == "stop":
            new_file.write("\n")
            sys.exit("EXIT")
        new_file.write(f"{count_lines} {content}\n")
        count_lines += 1


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(time_stamp())
        create_content(file)


if __name__ == "__main__":
    flags_choice()
