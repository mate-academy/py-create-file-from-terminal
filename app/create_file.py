import sys
import os
import datetime


arguments = sys.argv
index_f = None
index_d = None

for i in range(len(arguments)):
    if arguments[i] == "-f":
        index_f = i
    elif arguments[i] == "-d":
        index_d = i

if index_d is not None:
    end = len(arguments)
    if index_f is not None and index_f > index_d:
        end = index_f
    directories = arguments[index_d + 1: end]
    path = os.path.join(*directories)
    os.makedirs(path)


if index_f is not None:
    file_name = arguments[index_f + 1]
    if index_d is not None:
        file_name = os.path.join(path, file_name)
    new_line = False
    if os.path.exists(file_name):
        new_line = True
    with open(file_name, "a") as f:
        if new_line:
            f.write("\n")
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        count = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            count += 1
            f.write(f"{count} {line}\n")
