import sys
import os
from datetime import datetime


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


def f_flag(command: list) -> None:
    if "-f" in command and "-d" not in command:
        file_name = os.path.basename(os.path.join(*command[::]))
        write_line_in_file(file_name)


def d_flag(command: list) -> None:
    if "-d" in command and "-f" not in command:
        os.makedirs(os.path.join(*command[1:]), exist_ok=True)


def d_and_f_flags(command: list) -> None:
    if "-d" in command and "-f" in command:
        path = ""
        index_f_flag = command.index("-f")
        index_d_flag = command.index("-d")
        if index_f_flag > index_d_flag:
            path = os.path.join(*command[index_d_flag + 1:index_f_flag])
        if index_f_flag < index_d_flag:
            path = os.path.join(*command[index_d_flag + 1:])
        file_name = command[index_f_flag + 1]
        os.makedirs(path, exist_ok=True)
        write_line_in_file(os.path.join(path, file_name))


def execution_of_the_command() -> None:
    command = sys.argv[1:]
    f_flag(command=command)
    d_flag(command=command)
    d_and_f_flags(command=command)


if __name__ == "__main__":
    execution_of_the_command()
