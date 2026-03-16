import os
import sys
import datetime


def create_path(directories: list) -> str:
    return os.path.join(*directories)


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path: str, file_name: str) -> None:
    if path != "":
        file_name = os.path.join(path, file_name)
    time_now = datetime.datetime.now()
    page_number = 0
    next_text = ""
    if os.path.exists(file_name):
        next_text = "\n"
    with open(file_name, "a") as source_file:
        source_file.write(next_text)
        time_now = time_now.strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{time_now} \n")
        while True:
            text = input("Enter content line: ")
            page_number += 1
            if text.lower() == "stop":
                break
            source_file.write(f"{page_number} {text}\n")


list_argv = sys.argv

if len(list_argv) > 2:
    if "-d" in list_argv and "-f" in list_argv:
        path = create_path(list_argv[2:len(list_argv) - 2])
        create_directory(path)
        create_file(path, list_argv[-1])
    elif "-d" in list_argv:
        create_directory(create_path(list_argv[2:len(list_argv)]))
    elif "-f" in list_argv:
        create_file("", list_argv[2])
