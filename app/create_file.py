from sys import argv
from os import makedirs, getcwd
from datetime import datetime

args = argv
program_path = getcwd()
path = ""
i = 2

if "-d" in args:
    while args[i] != "-f":
        path += args[i] + "\\"
        i += 1
        if i == len(args):
            break
    makedirs(path, exist_ok=True)
    path = program_path + "\\" + path


if "-f" in args:
    file_name = args[i + 1]
    with open(f"{path}/{file_name}.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(str(timestamp) + "\n")

        page_number = 1
        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            file.write(f"{page_number} {line}" + "\n")
            page_number += 1
