import os
import sys
from datetime import datetime


def create_path(path: list) -> str:
    if "-d" in path and "-f" in path:
        directories = path[path.index("-d") + 1:path.index("-f")]
    else:
        directories = path[path.index("-d") + 1:]
    result = os.path.join(*directories)
    return result


# Directories creation:
if "-d" in sys.argv:
    directories_path = create_path(sys.argv)
if not os.path.exists(directories_path):
    os.makedirs(directories_path)
os.chdir(directories_path)

# File creation:
if "-f" in sys.argv:
    file_name = sys.argv[-1]
    open_type = "w" if not os.path.exists(file_name) else "a"
    with open(file_name, open_type) as file_in:
        file_in.write(
            f"{datetime.now().strftime('%Y-%m-%d %I:%M:%S')}\n"
        )
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file_in.write(f"{line_number} {content}\n")
            line_number += 1
        file_in.write("\n")
