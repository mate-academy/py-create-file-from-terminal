import sys
import os
import datetime

if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    path_parts = sys.argv[d_index + 1:]
    str_to_create = os.path.join(*path_parts)
    os.makedirs(str_to_create)
if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    with open(file_name, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            lines.append(line)
        for i in range(len(lines)):
            f.write(f"{i + 1} {lines[i]}\n")
