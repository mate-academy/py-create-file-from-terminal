import os
import sys
import datetime


def create_file() -> None:
    full_path = ""
    file_name = ""

    is_dir = False
    is_file = False

    for item in sys.argv:
        if item == "-d":
            is_dir = True
            is_file = False
            continue
        if item == "-f":
            is_dir = False
            is_file = True
            continue
        if is_dir:
            full_path = os.path.join(full_path, item)
        if is_file:
            file_name = item

    if not os.path.isdir(full_path):
        os.makedirs(full_path)

    if file_name == "":
        full_path = os.path.join(full_path, "file.txt")
    else:
        full_path = os.path.join(full_path, file_name)

    input_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    count = 0
    while input_str != "stop":
        temp_str = input("Enter content line: ")
        if temp_str == "stop":
            break
        count += 1
        input_str += str(count)
        input_str += " " + temp_str + "\n"
    input_str += "\n"

    with open(full_path, "a") as file:
        file.write(input_str)
