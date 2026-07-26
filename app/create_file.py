import sys
import os
from datetime import datetime

current_arg = None
directory_parts = None
file_name = None

for arg in sys.argv[1:]:

    if current_arg == "dir" and arg not in ("-d", "-f"):
        if directory_parts is None:
            directory_parts = [arg]
        else:
            directory_parts = directory_parts.append(arg)

    if current_arg == "file":
        file_name = arg

    if arg == "-d":
        current_arg = "dir"

    if arg == "-f":
        if file_name is not None:
            raise ValueError("File name already specified.")
        current_arg = "file"

if directory_parts is not None:
    directory_parts = os.path.join(*directory_parts)

    if not os.path.exists(directory_parts):
        os.makedirs(directory_parts)

if file_name is not None:
    file_path = file_name

    if directory_parts is not None:
        file_path = os.path.join(directory_parts, file_name)

    path_exists = os.path.exists(file_path)
    path_has_content = os.path.getsize(file_path) > 0

    with open(file_path, "a") as output_file:
        if path_exists and path_has_content:
            output_file.write("\n")

        output_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            output_file.write(f"{line_number} {line}\n")
            line_number += 1
