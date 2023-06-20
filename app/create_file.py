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

    dirs_path = ""

    if "-d" in command:
        d_index = command.index("-d")
        f_index = None
        if "-f" in command and command.index("-f") > d_index:
            f_index = command.index("-f")
        dirs = command[d_index + 1: f_index]
        dirs_path = os.path.join(*dirs)
        os.makedirs(dirs_path, exist_ok=True)

    if "-f" in command:
        f_index = command.index("-f")
        file_name = command[f_index + 1]
        file_path = os.path.join(dirs_path, file_name)
        write_to_file(file_path)


if __name__ == "__main__":
    create_file(entered_command)
