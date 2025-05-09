import sys
import os
from datetime import datetime


def create_file(name_file: str) -> None:
    if os.path.exists(name_file):
        with open(name_file, "a") as file:
            file.write("\n")
            file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            number_line = 1
            while True:
                pyting_line = input("Enter content line: ")
                if pyting_line == "stop":
                    break
                file.write(f"{number_line} {pyting_line}\n")
                number_line += 1
        return
    with open(name_file, "w") as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        number_line = 1
        while True:
            pyting_line = input("Enter content line: ")
            if pyting_line == "stop":
                break
            file.write(f"{number_line} {pyting_line}\n")
            number_line += 1


def create_file_or_dir(command: list) -> None:
    flag_f_index = command.index("-f") if "-f" in command else None
    flag_d_index = command.index("-d") if "-d" in command else None
    path = ""
    if flag_f_index is None and flag_d_index is None:
        print("Typing command!!!")
        return
    if flag_f_index is not None:
        if not (len(command) > flag_f_index + 1):
            print("Please typing name file with extension!!!")
            return
        if not command[flag_f_index + 1].endswith(".txt"):
            print("Please typing name file with extension!!!")
            return
    if flag_d_index is not None and flag_f_index is not None:
        path = "/".join(command[flag_d_index + 1:flag_f_index])
    elif flag_d_index is not None:
        path = "/".join(command[flag_d_index + 1:])
    if flag_d_index is not None:
        if not os.path.exists(path):
            os.makedirs(path)
        if flag_f_index is not None:
            path += f"/{command[flag_f_index + 1]}"
            create_file(path)
            return
    if flag_f_index is not None:
        create_file(command[flag_f_index + 1])
        return


if __name__ == "__main__":
    typing_command = sys.argv
    create_file_or_dir(typing_command)
