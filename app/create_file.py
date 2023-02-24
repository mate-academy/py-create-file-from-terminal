import os
import sys
import datetime


path, flag, *content = sys.argv


def create_dirs(*content) -> None:

    dirs_path = os.path.join(os.getcwd(), *content)
    if not os.path.exists(dirs_path):
        os.makedirs(dirs_path)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line_content = input("Enter content line: ")
            file.write(f"{line_number} {line_content}\n")
            line_number += 1
            if line_content == "stop":
                break


if "-f" in content:
    *content, _, file_name = content
    create_dirs(*content)
    create_file(os.path.join(os.getcwd(), *content, file_name))

if flag == "-d":
    create_dirs(*content)

if flag == "-f":
    create_file(os.path.join(os.getcwd(), *content))

create_dirs()
