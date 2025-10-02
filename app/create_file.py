import sys
import os
from datetime import datetime

current_arg = None
diretory = None
file_name = None

for arg in sys.argv[1:]:

    if current_arg == "dir" and arg not in ("-d", "-f"):
        if diretory is None:
            diretory = arg
        else:
            diretory = os.path.join(diretory, arg)

    if current_arg == "file":
        file_name = arg

    if arg == "-d":
        current_arg = "dir"

    if arg == "-f":
        current_arg = "file"

if diretory is not None:
    if not os.path.exists(diretory):
        os.makedirs(diretory)

if file_name is not None:
    file_path = file_name

    if diretory is not None:
        file_path = os.path.join(diretory, file_name)

    path_exists = os.path.exists(file_path)

    with open(file_path, "a") as f:
        if path_exists:
            f.write("\n")

        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        secstion = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{secstion} {line}\n")
            secstion += 1
