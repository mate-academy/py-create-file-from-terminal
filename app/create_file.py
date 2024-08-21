import os
import sys
from datetime import datetime


type_elem = ""
is_path = []
is_file = ""
path = ""
for elem in sys.argv:
    if elem == "-d":
        type_elem = "path"
        continue
    if elem == "-f":
        type_elem = "file"
        continue
    if type_elem == "path":
        is_path.append(elem)
    if type_elem == "file":
        is_file = elem

if is_path:
    path = os.path.join(*is_path)
    if not os.path.exists(path):
        os.makedirs(path)

if is_file:
    with open(os.path.join(path, is_file), "a") as file:
        file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} \n")
        num_line = 0
        while True:
            content = input("Enter content line: ")
            num_line += 1
            if content == "stop":
                file.write("\n")
                break
            file.write(f"{num_line} {content} \n")
