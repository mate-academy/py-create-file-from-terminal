import sys
import os
from datetime import datetime


dir_path = ""
file_name = ""

for i in range(len(sys.argv)):
    if sys.argv[i] == "-d":
        dir_path = "/".join(sys.argv[i + 1:])
        os.makedirs(dir_path)
    elif sys.argv[i] == "-f":
        file_name = sys.argv[i + 1]

    file_path = os.path.join(dir_path, file_name)
    mode = "a" if os.path.isfile(file_path) else "w"

    with open(file_path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
    i = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        file.write(f"{i} {content} \n")
        i += 1
