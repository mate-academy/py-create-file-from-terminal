import sys
import os
from datetime import datetime


arguments = sys.argv[1:]


def create_file_from_terminal(commands_list: list) -> None:
    path = os.getcwd()
    if "-d" in commands_list:
        for item in commands_list[1:]:
            if item.startswith("-"):
                break
            path = os.path.join(path, item)
        if not os.path.exists(path):
            os.makedirs(path)
    if "-f" in commands_list:
        file_name = commands_list[-1]
        path = os.path.join(path, file_name)
        if os.path.exists(path):
            write_argument = "a"
        else:
            write_argument = "w"
        with open(path, write_argument) as file:
            if write_argument == "w":
                current_datetime = datetime.now()
                formatted_datetime = current_datetime.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                file.write(formatted_datetime + "\n")
            count = 1
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                file.write(f"{count} " + text + "\n")
                count += 1


create_file_from_terminal(arguments)
