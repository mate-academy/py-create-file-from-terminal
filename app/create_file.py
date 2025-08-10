import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path)
    my_current_directory = os.getcwd()
    os.chdir(os.path.join(my_current_directory, path))


def create_file(file_name: str) -> None:
    count = 1
    file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_content += "\n" + str(count) + " " + line
        count += 1
    with open(file_name, "w") as file:
        file.write(file_content)


command = sys.argv

if "-d" in command:
    if "-f" not in command:
        path = os.path.join(*command[2:])
    else:
        path = os.path.join(*command[2:-2])
    create_directory(path)
if "-f" in command:
    file_name = command[-1]
    create_file(file_name)
