import sys
import os
import datetime


args = sys.argv[1:]
path = ""

if "-d" in args:
    index_of_d = args.index("-d")
    dirs = []

    for arg in range(index_of_d + 1, len(args)):
        if args[arg] == "-f":
            break
        dirs.append(args[arg])

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

file_name = ""

if "-f" in args:
    index_of_f = args.index("-f")

    if index_of_f + 1 < len(args):
        file_name = args[index_of_f + 1]
    else:
        print("Enter filename, please")

file_path = os.path.join(path, file_name) if path else file_name

with open(file_path, "a") as f:
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
    i = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        f.write(f"{i} {line}\n")
        i += 1
