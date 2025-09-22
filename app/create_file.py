import sys
import os
from datetime import datetime


if "-d" in sys.argv and "-f" in sys.argv:
    d_index = sys.argv.index("-d")
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    dirs = sys.argv[d_index + 1 : f_index]
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, file_name)
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S\n"))
        i = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{i} {line}\n")

elif "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    dirs = sys.argv[d_index + 1:]
    path = os.path.join(*dirs)
    if dirs:
        os.makedirs(path, exist_ok=True)

elif "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S\n"))
        i = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{i} {line}\n")
else:
    print("Please provide the -d (directories), -f (file), or both flags.")
