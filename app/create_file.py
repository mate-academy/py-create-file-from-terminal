import os
import sys
from datetime import datetime


def create_file_from_terminal(terminal: list[str]) -> None:
    full_path = ""
    if "-d" in terminal:
        full_path += crate_path(terminal)

    if "-f" in terminal:
        create_text_file(terminal, full_path)


def crate_path(terminal_command: list) -> str:
    full_path = ""

    index_d = 1
    index_f = 0
    for path in range(len(terminal_command)):
        if terminal_command[path] == "-d":
            index_d += path

        if terminal_command[path] == "-f":
            index_f += path

    if index_f != 0:
        directory = terminal_command[index_d:index_f]
    else:
        directory = terminal_command[index_d:]

    full_path += "/".join(directory)

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    return full_path


def create_text_file(terminal_command: list, full_path: str) -> None:
    name_file = ""
    for file_name in terminal_command:
        if ".txt" in file_name:
            name_file += file_name

    if full_path != "":
        name_file = full_path + "/" + name_file

    if ".txt" in name_file:
        with open(name_file, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")

            while True:
                line_char = 1
                input_data = str((input("Enter content line: ")))
                if input_data == "stop":
                    break
                data_file = str(line_char) + " " + input_data + "\n"
                line_char += 1
                file.write(data_file)
            file.write("\n")


create_file_from_terminal(terminal=sys.argv)
