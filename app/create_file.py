from datetime import datetime
import os
import sys

parent_dir = os.getcwd()
dir_ = []

time_now = datetime.now()
time_formated = time_now.strftime("%Y/%m/%d %H:%M:%S")

if "-f" in sys.argv and "-d" in sys.argv:
    copy = sys.argv
    d_index = copy.index("-d")
    f_index = copy.index("-f")
    directory = copy[d_index + 1:f_index]
    directoryy = str(directory)
    path = '/'.join(directory)
    name = copy[f_index + 1]
    final_path = os.path.join(path + '/' + name)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(final_path, "a+") as f:
        f.write(str(time_formated) + "\n")
        count = 1
        while True:
            content = input('Enter the line content:')
            if content == 'stop':
                f.write(" \n")
                break
            f.write(str(count) + " " + content + "\n")
            count += 1

elif "-d" in sys.argv:
    copy = sys.argv
    d_index = copy.index("-d")
    directory = copy[d_index + 1:]
    path = '/'.join(directory)
    os.makedirs(path)

elif "-f" in sys.argv:
    name = sys.argv[2]
    current_name = name
    with open(current_name, 'a+') as f:
        f.write(str(time_formated) + "\n")
        count = 1
        while True:
            content = input('Enter the line content:')
            if content == 'stop':
                f.write("\n")
                break
            f.write(str(count) + " " + content + "\n")
            count += 1
