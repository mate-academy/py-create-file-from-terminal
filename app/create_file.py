import datetime
import os
from sys import argv


def create_file(command: list[str]) -> None:
    if "-f" in command and "-d" in command:
        d_index = command.index("-d")
        f_index = command.index("-f")
        if d_index < f_index:
            dir_path = os.path.join(
                *command[d_index + 1:f_index]
            )
            os.makedirs(dir_path, exist_ok=True)
        else:
            dir_path = os.path.join(*command[d_index + 1:])
            os.makedirs(dir_path, exist_ok=True)

    elif "-d" in command:
        dir_path = os.path.join(*command[command.index("-d") + 1:])
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in command:
        file_name = command[command.index("-f") + 1]

        if "-d" in command:
            file_name = os.path.join(dir_path, file_name)

        file_exists = os.path.exists(file_name)

        with open(file_name, "a") as a_file:
            if file_exists:
                a_file.write("\n")

            current_data = datetime.datetime.now()
            a_file.write(current_data.strftime("%Y-%m-%d %H:%M:%S") + "\n")

            text_line = input("Enter content line: ")
            count = 0
            while text_line != "stop":
                count += 1
                a_file.write(f"{count} {text_line}\n")
                text_line = input("Enter content line: ")


command = argv
create_file(command)
