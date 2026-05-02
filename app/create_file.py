from sys import argv, exit
from os import makedirs, path
from datetime import datetime

#argv = ["app/create_file.py", " file.txt", "-f   ", " file.txt"]

if len(argv) <= 2 :
    print("Usage: -f <filename> or/and -d <directory>")
    exit(0)

filename = ""
directory = []
stop = False
content = []
line_number = 1

del argv[0]

for index in range(len(argv)):
    if argv[index].strip() == "-f":
        try:
            filename = argv[index + 1].strip().lower()
            del argv[index: index + 2]
            break
        except IndexError:
            print("Error: correct format -f <filename>")
            exit(1)

for index in range(len(argv)):
    if argv[index].strip() == "-d":
        if index == len(argv) - 1:
            print("Error: correct format -d <directory name(s)>")
            exit(1)
        directory = [name.strip() for name in argv[index + 1:]]

print(f"Path: {path.join(*directory, filename)}")
print(f"file: {filename}")

if directory != []:
    makedirs(path.join(*directory), exist_ok=True)

if filename != "":
    full_path = path.join(*directory,filename)

    while not stop:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            stop = True
        else:
            content.append(f"{line_number} {line}\n")
            line_number += 1
    content.append("\n")

    with open(full_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in content:
            f.write(line)

