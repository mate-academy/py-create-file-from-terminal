import sys
import os
from datetime import datetime


arguments = sys.argv[1:]


if "-d" in arguments:
    d_index = arguments.index("-d")

    if "-f" in arguments:
        f_index = arguments.index("-f")
        dirs = arguments[d_index + 1:f_index]
        file_name = arguments[f_index + 1]
    else:
        dirs = arguments[d_index + 1:]

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, file_name)

    if "-f" in arguments:
        f_index = arguments.index("-f")
        file_name = arguments[f_index + 1]
        with open(file_name, "a") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            lines = []
            while True:
                line = input("Enter content line:")
                if line == "stop":
                    break
                lines.append(line)
            for i, line in enumerate(lines, start=1):
                f.write(f"{i} {line}\n")


