import sys
import os
import datetime


directory = "./"
if "-d" in sys.argv:
    index_need = sys.argv.index("-d") + 1
    dir_parts = []
    for arg in sys.argv[index_need:]:
        if arg.startswith("-"):
            break
        dir_parts.append(arg)
    directory = os.path.join(directory, *dir_parts)
    os.makedirs(directory)

if "-f" in sys.argv:
    index_need = sys.argv.index("-f") + 1
    with open(f"{directory}/{sys.argv[index_need]}", "a") as file:
        file.write(f"{datetime.datetime.now()}\n")
        line_number = 1
        while True:
            text = str(input("Enter content line: "))
            if text.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {text}\n")
            line_number += 1
