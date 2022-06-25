import sys
import os
from datetime import datetime
from pathlib import Path

dir_ = f"{Path(__file__).resolve().parent.parent}"
time = datetime.now().strftime("%Y-%m-%d %I:%M:%S")
content = f"{time}\n"
count = 0
while True:
    inp = input('Enter content line: ')
    if inp != "stop":
        count += 1
        content += str(count) + " " + inp + "\n"
    else:
        break

argv = sys.argv


def iterator_by_dir():
    global dir_
    for i in range(ind_d + 1, len(argv) - ind_d + 1):
        if argv[i] == "-f":
            break
        else:
            dir_ = dir_ + os.path.join(f"\\{argv[i]}")
            if os.path.isdir(dir_):
                pass
            else:
                os.mkdir(dir_)


def file_a_and_w(file="file.txt"):
    global dir_
    dir_ = dir_ + os.path.join(f"\\{file}")
    if os.path.isfile(dir_):
        with open(dir_, "a") as f:
            f.write(content)
    else:
        with open(dir_, "w") as f:
            f.write(content)


if "-d" in argv and "-f" in argv:
    ind_d = argv.index("-d")
    ind_f = argv.index("-f")
    iterator_by_dir()
    file_a_and_w(argv[ind_f + 1])

else:
    if "-f" in argv:
        ind = argv.index("-f")
        file_a_and_w(argv[ind + 1])

    if "-d" in argv:
        ind_d = argv.index("-d")
        iterator_by_dir()
        file_a_and_w()
