import os
import sys
from datetime import datetime


def create_file_from_input():
    terminal = sys.argv
    path = ""
    for i, command in enumerate(terminal[1:]):
        if command == "-f":
            write_content_to_file(terminal[i + 2], path)
            break
        elif command != "-d":
            path += f"/{command}"


def write_content_to_file(name_file, dir_path):
    if dir_path:
        if not os.path.exists(f"app{dir_path}"):
            os.makedirs(f"app{dir_path}")
        dir_path = "app" + dir_path + "/"

    with open(dir_path + name_file, "a") as file:
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y, %H:%M:%S\n")
        file.write(date_time)
        while True:
            new_content = input("Enter content line: ")
            if new_content.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{new_content}\n")


create_file_from_input()
