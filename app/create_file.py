import os
import sys
from datetime import datetime

args = sys.argv
file_name = ""
dir_path = ""

if len(args) >= 3 and args[1] == "-d":
    is_f = False
    for arg in args[2:]:
        if arg == "-f":
            is_f = True
            continue
        if is_f:
            file_name = arg
            break

        dir_path = os.path.join(dir_path, arg)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

elif len(args) >= 3 and args[1] == "-f":
    file_name = args[2]

if file_name:
    if dir_path:
        file_name = os.path.join(dir_path, file_name)

    with open(file_name, "a") as f:
        date = datetime.now()
        f.write(date.strftime("%Y-%m-%d %H:%M:%S\n"))
        text = input("Enter content line:")
        is_stop = text.lower()
        i = 1
        while is_stop != "stop":
            f.write(f"{str(i)}. {text}\n")
            text = input("Enter content line:")
            i += 1
            is_stop = text.lower()
