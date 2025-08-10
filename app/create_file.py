import sys
import os
from datetime import datetime


def create_file_from_terminal() -> None:
    command = sys.argv
    dir_path = ""
    file_name = ""

    if "-d" in command and "-f" not in command:
        dir_path = "/".join(command[1:])
    if "-f" in command and "-d" not in command:
        file_name = command[1]
    if "-d" in command and "-f" in command:
        f_index, d_index = command.index("-f"), command.index("-d")
        dir_path = "/".join(command[d_index:f_index])
        file_name = command[f_index + 1]

    dst_path = os.path.join(dir_path, file_name)
    os.makedirs(dst_path)

    with open(file_name, "a") as file:
        current_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        file.write(current_date)

        line_number = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file.write(f"{line_number} {line_content}\n")
            line_number += 1


if __name__ == "__main__":
    create_file_from_terminal()
