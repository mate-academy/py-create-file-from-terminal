import os
import sys
import datetime


entered_command = sys.argv[1:]


def write_to_file(path_to_file: str) -> None:
    current_date = datetime.datetime.now()
    content = str(current_date.strftime("%Y-%m-%d %H:%M:%S")) + "\n"
    user_input = ""
    line_number = 1
    while user_input != "stop":
        user_input = input("Enter content line: ")
        if user_input != "stop":
            content += f"{line_number} {user_input}\n"
            line_number += 1
    content += "\n"
    with open(path_to_file, "a") as file:
        file.write(content)


def create_file(command: list) -> None:

    file_name = command[-1]
    dirs_path = ""

    if "-d" in command:
        f_index = None
        for idx, item in enumerate(command):
            if item == "-f":
                f_index = idx
        dirs = command[1: f_index]
        dirs_path = os.path.join(*dirs)
        os.makedirs(dirs_path, exist_ok=True)
        if "-f" not in command:
            return

    file_path = os.path.join(dirs_path, file_name)
    write_to_file(file_path)


if __name__ == "__main__":
    create_file(entered_command)
