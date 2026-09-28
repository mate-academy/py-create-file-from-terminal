import os
import sys

from datetime import datetime


_, *commands = sys.argv
content = " ".join(commands)

correct_dir = os.getcwd()
today_time = datetime.now()

if "-d" in content and "-f" in content:
    index_d = content.index("-d")
    index_f = content.index("-f")

    if index_d < index_f:
        d_place, f_place = content.find("-d"), content.find("-f")
        file_name = content[f_place + 2:].strip()

        connect_dir_path = content[d_place + 2: f_place].split()
        directory_name = os.path.join(correct_dir, *connect_dir_path)

    else:
        start, end = content.find("-f"), content.find("-d")
        file_name = content[start + 2:end].strip()

        connect_dir_path = content[end + 2:].split()
        directory_name = os.path.join(correct_dir, *connect_dir_path)

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    file_name = os.path.join(directory_name, file_name)
    file_exist = os.path.isfile(file_name)

    with open(file_name, "a") as file:

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

elif "-d" in content:
    d_place = content.find("-d")

    connect_dir_path = content[d_place + 2:].split()
    directory_name = os.path.join(correct_dir, *connect_dir_path)

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

elif "-f" in content:
    f_place = content.find("-f")
    file_name = content[f_place + 2:].strip()
    file_exist = os.path.isfile(file_name)

    with open(file_name, "a") as file:

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
