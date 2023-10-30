import os
import sys
from datetime import datetime

args = sys.argv
file_name = ""
dir_path = ""

if len(args) >= 3 and args[1] == "-d":
    for i in range(2, len(args)):
        if args[i] == "-f":
            if (i + 1) <= len(args) - 1:
                file_name = args[i + 1]
            break

        dir_path += args[i] + "\\"

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

elif len(args) >= 3 and args[1] == "-f":
    file_name = args[2]

if file_name:
    if dir_path:
        file_name = dir_path + file_name

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
