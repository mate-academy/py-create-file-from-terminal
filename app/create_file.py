import os
import sys
from datetime import datetime


def create_file_or_append_to_existing(file_name: str, mode: str) -> None:
    my_file = open(file_name, mode)
    count = 1
    my_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    while True:
        input_str = str(input("Enter content line: "))
        if input_str != "stop":
            my_file.write(f"{count} {input_str}\n")
        else:
            break
        count += 1
    my_file.close()


def create_file_from_terminal() -> None:
    commands_dict = {}
    if "-d" in sys.argv[1:] and "-f" not in sys.argv[1:]:
        if "-" not in sys.argv[1:]:
            commands_dict["-d"] = sys.argv[1:][sys.argv[1:].index("-d") + 1:]
        else:
            commands_dict["-d"] = sys.argv[1:][sys.argv[1:].index("-d") + 1:
                                               sys.argv[1:].index("-")]
    if "-f" in sys.argv[1:] and "-d" not in sys.argv[1:]:
        commands_dict["-f"] = sys.argv[1:][sys.argv[1:].index("-f") + 1:]
    if "-d" in sys.argv[1:] and "-f" in sys.argv[1:]:
        commands_dict["-d"] = sys.argv[1:][sys.argv[1:].index("-d") + 1:
                                           sys.argv[1:].index("-f")]
        commands_dict["-f"] = sys.argv[1:][sys.argv[1:].index("-f") + 1:]
    dir_path = ""
    file_name = ""
    if "-d" in commands_dict:
        dir_path = f"{'/'.join(commands_dict['-d'])}"
    if "-f" in commands_dict:
        file_name = f"{'/'.join(commands_dict['-f'])}"
    if dir_path and not file_name:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    if file_name and dir_path:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.isfile(f"{dir_path}/{file_name}"):
            create_file_or_append_to_existing(f"{dir_path}/{file_name}", "w")
        else:
            create_file_or_append_to_existing(f"{dir_path}/{file_name}", "a")
    if file_name and not dir_path:
        if not os.path.isfile(file_name):
            create_file_or_append_to_existing(file_name, "w")
        else:
            create_file_or_append_to_existing(file_name, "a")


create_file_from_terminal()
