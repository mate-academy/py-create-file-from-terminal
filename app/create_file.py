from datetime import datetime

import os
import sys


working_directory = os.getcwd()
if "-d" in sys.argv:
    for line in range(2, len(sys.argv)):
        if sys.argv[line] == "-f":
            break
        working_directory = os.path.join(working_directory, sys.argv[line])
    os.mkdir(working_directory)

if "-f" in sys.argv:
    current_file = os.path.join(working_directory, sys.argv[-1])
    with open(current_file, "a") as current_new_file:
        current_new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_number = 1
        while True:
            input_string = input("Enter content line:")
            if input_string.lower() == "stop":
                break
            current_new_file.write(f"{line_number} {input_string}")
            line_number += 1
