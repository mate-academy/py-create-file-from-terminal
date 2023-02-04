import sys
import os
from datetime import datetime

COMMAND = sys.argv[1:]


def write_line_in_file(file_path: str) -> None:
    with open(file_path, "a") as file_in:
        file_in.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S \n"))
        count_line = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            count_line += 1
            file_in.write(f"{count_line} {content}\n")
        file_in.write("\n")


def execution_of_the_command() -> None:
    path = ""
    file_name = ""
    if "-f" in COMMAND and "-d" not in COMMAND:
        file_name = os.path.basename(os.path.join(*COMMAND[::]))
    if "-d" in COMMAND and "-f" not in COMMAND:
        if os.path.exists(os.path.join(*COMMAND[1:])) is False:
            os.makedirs(os.path.join(*COMMAND[1:]))
        return
    if "-d" in COMMAND and "-f" in COMMAND:
        index_f_flag = COMMAND.index("-f")
        index_d_flag = COMMAND.index("-d")
        if index_f_flag > index_d_flag:
            path = os.path.join(*COMMAND[index_d_flag + 1:index_f_flag])
        if index_f_flag < index_d_flag:
            path = os.path.join(*COMMAND[index_d_flag + 1:])
        file_name = COMMAND[index_f_flag + 1]
        if os.path.exists(os.path.join(path)) is False:
            os.makedirs(path)
    path_with_file = os.path.join(path, file_name)
    write_line_in_file(path_with_file)


if __name__ == "__main__":
    execution_of_the_command()
