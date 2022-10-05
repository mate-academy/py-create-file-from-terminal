import datetime
import os
from sys import argv


directory = []
file_name = ""

if "-f" in argv:
    file_name = str(argv[argv.index("-f") + 1:])
    if "-d" in argv:
        directory = argv[argv.index("-d") + 1:argv.index("-f")]
else:
    directory = argv[argv.index("-d") + 1:]

if directory:
    directory = "/".join(directory)
    os.makedirs(directory)
    os.chdir(directory)

if file_name:
    with open(file_name, "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        while True:
            file_content = input("Enter content line: ")
            if file_content == "stop":
                break
            file.write(f"{file_content}\n")
        file.write("\n")
