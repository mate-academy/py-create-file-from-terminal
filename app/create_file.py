import os
import sys
from datetime import datetime

current_directory = ""
if sys.argv[1] == "-d":
    for subdirectory in sys.argv[2::]:
        if subdirectory == "-f":
            break
        current_directory = os.path.join(subdirectory, current_directory)
        os.mkdir(current_directory)


if "-f" in sys.argv:
    new_file = os.path.join(current_directory, sys.argv[-1])
    with open(new_file, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
