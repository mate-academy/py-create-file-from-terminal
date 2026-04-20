import os
import sys
from datetime import datetime


def create_dir(dir_name: list) -> str:
    current_path = ""
    for dir_ in dir_name:
        current_path = os.path.join(current_path, dir_)
        if not os.path.exists(current_path):
            os.makedirs(current_path)
    return str(current_path)


def create_file(file_name: str) -> None:
    i_numerating = 1
    with open(file_name, "a") as result_file:
        result_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S" + "\n"))
        while True:
            str_input = input("Enter content line: ")
            if str_input == "stop":
                result_file.write("\n")
                break
            result_file.write(f"{i_numerating} " + str_input + "\n")
            i_numerating += 1


def get_and_executing_command() -> None:
    full_command = sys.argv
    start_dir, end_dir, start_file = 0, 0, 0
    if "-d" in full_command:
        start_dir = full_command.index("-d") + 1
        end_dir = len(full_command)
    if "-f" in full_command:
        start_file = full_command.index("-f") + 1
        end_dir = full_command.index("-f")
    if start_dir > start_file :
        end_dir = len(full_command)
    if start_dir != 0 and end_dir != 0 and start_file != 0:
        directory_path = create_dir(full_command[start_dir:end_dir])
        create_file(os.path.join(str(directory_path),
                                 full_command[start_file]))
        return
    if start_dir != 0 and end_dir != 0:
        create_dir(full_command[start_dir:end_dir])
        return
    if start_file != 0:
        create_file(os.path.join(os.getcwd(), full_command[start_file]))


get_and_executing_command()
