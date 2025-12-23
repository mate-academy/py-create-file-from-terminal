import os
import datetime
import sys


args = sys.argv[1:]
new_dir = []
new_file = ""

ind = 0
while ind < len(args):
    if args[ind] == "-d":
        ind += 1
        parts = []
        while ind < len(args) and not args[ind].startswith("-"):
            parts.append(args[ind])
            ind += 1
        new_dir = parts
        continue
    if args[ind] == "-f":
        ind += 1
        if ind < len(args):
            new_file = args[ind]
            ind += 1
        else:
            raise TypeError("Invalid file name")
        continue
    ind += 1

if new_dir:
    new_dir_path = os.path.join(*new_dir)
    os.makedirs(new_dir_path, exist_ok=True)
    os.chdir(new_dir_path)

if new_file:
    with open(new_file, "a") as file:
        if os.path.exists(new_file) and os.path.getsize(new_file) > 0:
            file.write("\n")
        current_date = datetime.datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        message = input("Enter content line: ")

        count = 1
        while message != "stop":
            file.write(f"{count} {message}\n")
            count += 1
            message = input("Enter content line: ")
