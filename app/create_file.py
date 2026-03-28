import sys
import os
from datetime import datetime


flag_d = False
flag_f = False
directories = []
files = []

for arg in sys.argv[1:]:
    if arg == "-d":
        flag_d = True
        flag_f = False
        continue
    if arg == "-f":
        flag_f = True
        flag_d = False
        continue
    if arg.startswith("-"):
        flag_d = False
        flag_f = False
        continue
    if flag_d:
        directories.append(arg)
    elif flag_f:
        files.append(arg)

path = ""
if directories:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

for file_name in files:
    with open(os.path.join(path, file_name), "w") as file:
        content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        line = 1
        while True:
            user_input = input("Enter content line: ").strip()
            if user_input.lower() == "stop":
                break
            content += f"{line} {user_input}\n"
            line += 1
        file.write(content)
