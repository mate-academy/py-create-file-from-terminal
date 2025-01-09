import os
import sys
from datetime import datetime

arguments = sys.argv

if "-d" in arguments and "-f" in arguments:
    d_index = arguments.index("-d")
    f_index = arguments.index("-f")
    path = os.path.join(*arguments[d_index + 1:f_index])
    os.makedirs(path, exist_ok=True)
else:
    path = "."

if "-f" in arguments:
    f_index = arguments.index("-f")
    file_name = arguments[f_index + 1]
    file_path = os.path.join(path, file_name)

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")
        file.write(f"{timestamp}\n")

        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_num} {line}\n")
            line_num += 1
    print(f"File {file_path} created/updated.")
else:
    print("Error: No file name provided.")