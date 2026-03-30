import os
import sys
from datetime import datetime


"""
python  D:\\Mate_Academy\\Python_core\\Basic-modules-overview\\py-create-file-from-terminal\\app\\create_file.py -f file.txt

python create_file.py -d dir1 dir2
"""

current_file = sys.argv[0]

if len(sys.argv) == 3 and sys.argv[1] == "-f":
    file_to_create = sys.argv[2]
    with open(file_to_create, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        f.write(timestamp)
        i = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                sys.exit()
            f.write(f"{i} {line} \n")
            i += 1
elif len(sys.argv) == 4 and sys.argv[1] == "-d":
    print("i`m here!")
    dir_to_create = sys.argv[2]
    nested_dir_to_create = sys.argv[3]
    try:
        path_for_dirs = sys.argv[2] + "\\" + sys.argv[3]
        os.makedirs(path_for_dirs)
    except FileExistsError:
        pass

elif "-d" and "-f" in sys.argv:
    path_for_dirs = sys.argv[2] + "\\" + sys.argv[3]
    try:
        os.makedirs(path_for_dirs)
    except FileExistsError:
        pass
    file_to_create = path_for_dirs + '\\' + sys.argv[5]
    with open(file_to_create, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        f.write(timestamp)
        i = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                sys.exit()
            f.write(f"{i} {line} \n")
            i += 1

