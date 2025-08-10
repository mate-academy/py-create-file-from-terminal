import os
import sys
import datetime

path, flag, *content = sys.argv


def create_dirs(*content) -> None:
    dirs_path = os.path.join(os.getcwd(), *content)
    os.makedirs(dirs_path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line_content}\n")
            line_number += 1


if "-f" in content:
    *content, _, file_name = content
    create_dirs(*content)
    create_file(os.path.join(os.getcwd(), *content, file_name))

if flag == "-d":
    create_dirs(*content)

if flag == "-f":
    create_file(os.path.join(os.getcwd(), *content))

create_dirs()
