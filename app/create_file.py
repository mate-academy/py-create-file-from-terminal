import sys
import os
from datetime import datetime


dir_path = ""
file_name = ""

for string in range(len(sys.argv)):
    if sys.argv[string] == "-d":
        dir_path = "/".join(sys.argv[string + 1:])
        os.makedirs(dir_path)
    elif sys.argv[string] == "-f":
        file_name = sys.argv[string + 1]

    file_path = os.path.join(dir_path, file_name)
    mode = "a" if os.path.isfile(file_path) else "w"

    with open(file_path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
    counter = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        file.write(f"{counter} {content} \n")
        counter += 1
