import os
import sys
from datetime import datetime


type_elem = ""
is_path = []
is_file = ""
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
        file_name = elem

if is_path:
    path = os.path.join(is_path)
    if not os.path.exists(path):
        os.makedirs(path)

if is_file:
    with open(is_file, "w") as file:
        file.write(datetime.now().strftime())
        content = input("Enter content line: ")
        num_line = 1
        while True:
            if content == "stop":
                file.write("")
                break
            file.write(f"{num_line} {content}")
