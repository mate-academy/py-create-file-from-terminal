from datetime import datetime
import os
import sys

parent_dir = r"C:\PytyhonLearn\py-create-file-from-terminal\app"
dir_ = []

time = datetime.now()
timee = time.strftime("%Y/%m/%d %H:%M:%S")

if "-f" in sys.argv and "-d" in sys.argv:
    copy = sys.argv
    d_index = copy.index("-d")
    f_index = copy.index("-f")
    dir_ = copy[d_index + 1:f_index]
    path = '/'.join(dir_)
    name = copy[f_index + 1]
    os.makedirs(path)
    final_path = path + '/' + name
    with open(final_path, "w") as f:
        f.write(str(timee) + "\n")
        count = 1
        while True:
            content = input('Enter the line content:')
            if content == 'stop':
                break
            f.write(str(count) + " " + content + "\n")
            count += 1

elif "-d" in sys.argv:
    copy = sys.argv
    d_index = copy.index("-d")
    dir_ = copy[d_index + 1:]
    path = '/'.join(dir_)
    os.makedirs(path)

elif "-f" in sys.argv:
    name = sys.argv[2]
    current_name = name + '.txt'
    with open(current_name, 'w') as f:
        f.write(str(timee) + "\n")
