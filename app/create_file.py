import os
import sys
from datetime import datetime


def create_dir(dirs):
    path = os.path.join(*dirs)
    os.makedirs(path)


def create_file(name):
    formatted_datetime = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    with open(name, "a") as file:
        count_number = 1
        file.write(formatted_datetime + "\n")
        while True:
            user_input = str(input('Write your string (or "stop" for ending): '))
            if user_input.lower() == "stop":
                break
            file.write(f"{count_number} {user_input} + \n")
            count_number += 1


def find_argument():
    terminal_data = sys.argv
    if "-d" in terminal_data and "-f" in terminal_data:
        create_dir(terminal_data[2:-2])
        file_path = os.path.join(*terminal_data[2:-2], terminal_data[-1])
        create_file(file_path)
    elif "-d" in terminal_data and "-f" not in terminal_data:
        create_dir(terminal_data[2:])
    elif "-f" in terminal_data and "-d" not in terminal_data:
        create_file(terminal_data[-1])


if __name__ == "__main__":
    find_argument()
