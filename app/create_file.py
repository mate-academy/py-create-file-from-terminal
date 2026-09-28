import os
import sys

from datetime import datetime


_, *commands = sys.argv
content = " ".join(commands)

correct_dir = os.getcwd()
today_time = datetime.now()


def write_contents(file_path: str) -> None:
    with open(file_path, "a") as file:

        if file_exist:
            file.write("\n")

        file.write(today_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        number = 1

        while True:
            request_content = input("Enter content line: ")

            if request_content.lower() == "stop":
                break

            file.write(f"{number} {request_content}\n")
            number += 1


if "-d" in content and "-f" in content:
    d_index = content.index("-d")
    f_index = content.index("-f")

    if d_index < f_index:
        d_place, f_place = content.find("-d"), content.find("-f")
        file_name = content[f_place + 2:].strip()

        dir_parts = content[d_place + 2: f_place].split()
        directory_name = os.path.join(correct_dir, *dir_parts)

    else:
        d_place, f_place = content.find("-f"), content.find("-d")
        file_name = content[d_place + 2:f_place].strip()

        dir_parts = content[f_place + 2:].split()
        directory_name = os.path.join(correct_dir, *dir_parts)

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    file_name = os.path.join(directory_name, file_name)
    file_exist = os.path.isfile(file_name)

    write_contents(file_name)

elif "-d" in content:
    d_place = content.find("-d")

    dir_parts = content[d_place + 2:].split()
    directory_name = os.path.join(correct_dir, *dir_parts)

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

elif "-f" in content:
    f_place = content.find("-f")
    file_name = content[f_place + 2:].strip()
    file_exist = os.path.isfile(file_name)

    write_contents(file_name)
