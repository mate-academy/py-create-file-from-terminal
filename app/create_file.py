from datetime import datetime
from sys import argv
from os import mkdir, chdir

filename = ""
directories = []
create = True
if "-f" in argv:
    filename = argv[argv.index("-f") + 1]
    if "-d" in argv:
        directories = argv[argv.index("-d") + 1:argv.index("-f")]
else:
    filename = "file.txt"
    if "-d" in argv:
        directories = argv[argv.index("-d") + 1:len(argv)]
        create = False

file_data = [datetime.today().strftime("%y-%m-%d %H:%M:%S"), "\n"]

for directory in directories:
    try:
        mkdir(directory)
    except FileExistsError:
        pass
    chdir(directory)

if create is True:
    while True:
        line = input("Enter content line: ")
        if line == "exit":
            break
        file_data.extend([line, "\n"])
    with open(filename, "w") as file:
        file.writelines(file_data)
