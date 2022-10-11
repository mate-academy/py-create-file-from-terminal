from datetime import datetime
from sys import argv
from os import mkdir, chdir


filename = ""
directories = []

if "-f" in argv:
    filename = argv[argv.index("-f") + 1]
    if "-d" in argv:
        directories = argv[argv.index("-d") + 1:argv.index("-f")]
else:
    if "-d" in argv:
        directories = argv[argv.index("-d") + 1:len(argv)]

for directory in directories:
    try:
        mkdir(directory)
    except FileExistsError:
        pass
    chdir(directory)

if filename:
    file_data = [f"{datetime.today().strftime('%y-%m-%d %H:%M:%S')}\n"]
    line_num = 0
    while True:
        line_num += 1
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_data.extend(f"{line_num} {line}\n")

    with open(filename, "w") as file:
        file.writelines(file_data)
