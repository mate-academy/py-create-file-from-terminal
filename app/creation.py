import os
from datetime import datetime


def create_file(find_name: list, destination: list = None) -> None:
    if destination is None:
        destination = [""]
    file_name = ""
    for name in find_name:
        if "txt" in name:
            file_name = name
    with open(os.path.join(*destination, file_name), "a") as source_file:
        source_file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S") + "\n")
        while True:
            new_str = input("Enter: ")
            if new_str == "stop":
                source_file.write("\n")
                break
            source_file.write(new_str + "\n")


def create_dir(cmd: list) -> list:
    dir_list = []
    for dirs in cmd:
        if ".py" in dirs or "-d" in dirs or "-f" in dirs or "txt" in dirs:
            continue
        dir_list.append(dirs)
    os.makedirs(os.path.join(*dir_list), exist_ok=True)
    return dir_list
