import sys
import os
from datetime import datetime


def create_file() -> None:
    command_list = sys.argv
    current_dir = os.getcwd()
    if "-d" in command_list:
        for index in range(command_list.index("-d") + 1, len(command_list)):
            if command_list[index] == "-f":
                break

            current_dir = os.path.join(current_dir, command_list[index])
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
    if "-f" in command_list:
        if "." in command_list[command_list.index("-f") + 1]:
            current_dir = os.path.join(
                current_dir,
                command_list[command_list.index("-f") + 1]
            )
    try:
        with open(current_dir, "a") as current_file:
            count = 1
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            current_file.write(f"{current_time}\n")
            content = input("Enter content line: ")
            while content != "stop":
                current_file.write(f"{count} {content}\n")
                content = input("Enter content line: ")
                count += 1
            current_file.write("\n")
    except FileNotFoundError:
        print("file name not existing")


create_file()
