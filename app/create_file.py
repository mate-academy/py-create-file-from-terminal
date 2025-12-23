import os
import datetime
import sys


args = sys.argv[1:]
new_dir = []
new_file = ""

if "-d" in args and "-f" in args:
    d_index = args.index("-d")
    f_index = args.index("-f")
    new_dir = args[d_index + 1:f_index]
    if f_index + 1 < len(args):
        new_file = args[f_index + 1]
elif "-d" in args:
    d_index = args.index("-d")
    new_dir = args[d_index + 1:]
elif "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args):
        new_file = args[f_index + 1]

if new_dir:
    new_dir_path = os.path.join(*new_dir)
    os.makedirs(new_dir_path, exist_ok=True)
    os.chdir(new_dir_path)

if new_file:
    with open(new_file, "a") as file:
        current_date = datetime.datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        message = input("Enter content line: ")

        count = 1
        while message != "stop":
            file.write(f"{count} {message}\n")
            count += 1
            message = input("Enter content line: ")
