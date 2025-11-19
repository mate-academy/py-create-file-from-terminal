import sys
import os
import datetime

if "-d" in sys.argv:
    index_d = sys.argv.index("-d")
    if "-f" in sys.argv:
        index_f = sys.argv.index("-f")
        folder = sys.argv[index_d + 1: index_f]
    else:
        folder = sys.argv[index_d + 1:]
if "-f" in sys.argv:
    index_f = sys.argv.index("-f")
    file_path = sys.argv[index_f + 1]

if folder:
    directory = os.path.join(*folder)
    os.makedirs(directory, exist_ok=True)
if file_path:
    if directory:
        full_file = os.path.join(directory, file_path)
    else:
        full_file = file_path
    with open(full_file, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            f.write(str(count) + " " + content + "\n")
            count += 1
