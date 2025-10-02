import sys
import os
from datetime import datetime

for arg in sys.argv[1:]:
    current_arg = None
    diretory = None
    file_name = None

    if current_arg == "dir":
        if diretory is None:
            diretory = arg
        else:
            os.path.join(diretory, arg)

    if current_arg == "file":
        file_name = arg

    if arg == "-d":
        current_arg = "dir"

    if arg == "-f":
        current_arg = "file"

if diretory is not None:
    if not os.path.exists(diretory):
        os.makedirs(diretory)

elif file_name is not None:
    file_path = file_name

    if diretory is not None:
        file_path = os.path.join(diretory, file_name)

    with open(file_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(line + "\n")
