import os
import sys

from datetime import datetime


_, *content = sys.argv

if "-d" in content and "-f" in content:
    today_time = datetime.now()
    file_name = content[-1]
    directory_name = content[-3]

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
    directory_name = content[-1]

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

elif "-f" in content:
    today_time = datetime.now()
    file_name = content[-1]
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
