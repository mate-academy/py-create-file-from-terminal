import sys
import os
from datetime import datetime


directories = []
if "-d" in sys.argv:
    for i in sys.argv[sys.argv.index("-d") + 1:]:
        if i == "-f":
            break
        else:
            directories.append(i)

if "-f" in sys.argv:
    index_f = sys.argv.index("-f") + 1
    if index_f < len(sys.argv):
        file_name = (sys.argv[sys.argv.index("-f") + 1])
        if directories:
            file_path = os.path.join(*directories, file_name)
        else:
            file_path = file_name

if "-d" in sys.argv:
    index_d = sys.argv.index("-d") + 1
    if index_d < len(sys.argv):
        if directories:
            directories_path = os.path.join(*directories)
            os.makedirs(directories_path, exist_ok=True)

if "-f" in sys.argv:
    counter = 1
    with open(file_path, "a") as file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            word = input("Enter content line: ")
            if word.lower() == "stop":
                break
            file.write(str(counter) + " " + word + "\n")
            counter += 1
