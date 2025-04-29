from datetime import datetime
import os
import sys


def write_from_input(file_name: str) -> None:
    write_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    while True:
        text_input = input("Enter content line: ")
        if text_input == "stop":
            break
        write_text += text_input + "\n"
    print(write_text)
    with open(file_name, "a") as file:
        file.write(write_text)


def create_file() -> None:
    terminal_list = sys.argv[1:]

    if "-d" in terminal_list and "-f" in terminal_list:
        if terminal_list[0] == "-d":
            file_path = "/".join(terminal_list[1:-2])
            file_name = terminal_list[-1]
        else:
            file_path = "/".join(terminal_list[3:])
            file_name = terminal_list[1]
        os.makedirs(file_path, exist_ok=True)
        write_from_input(file_path + "/" + file_name)
        return None
    elif "-f" in terminal_list:
        file_name = terminal_list[1]
        write_from_input(file_name)
    elif "-d" in terminal_list:
        file_path = "/".join(terminal_list[1:])
        os.makedirs(file_path, exist_ok=True)


create_file()
