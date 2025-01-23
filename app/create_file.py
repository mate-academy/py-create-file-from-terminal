import os
import sys
from datetime import datetime


def text_test() -> None:
    print(sys.argv)
    dict_one = sys.argv
    file = None
    for i in dict_one:
        if i == "-f":
            file_index = dict_one.index("-f") + 1
            if file_index < len(dict_one):
                file = dict_one[file_index]
    dirs = []
    if "-d" in dict_one:
        dir_index = dict_one.index("-d") + 1
        while (dir_index < len(dict_one)
               and not dict_one[dir_index].startswith("-")):
            dirs.append(dict_one[dir_index])
            dir_index += 1

    directory_path = None
    if dirs:
        directory_path = "/".join(dirs)
        os.makedirs(directory_path, exist_ok=True)
    if file:
        file_path = os.path.join(directory_path,
                                 file) if  directory_path else file
        mode = "a" if os.path.exists(file_path) else "w"

        with open(file_path, mode) as f:
            current_date = datetime.now()
            timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n{timestamp}\n")
            number = 1
            while True:
                name = input(f"Enter content line: ")
                if name.lower() == "stop":
                    return 0
                f.write(f"{number} {name}\n")
                number += 1
