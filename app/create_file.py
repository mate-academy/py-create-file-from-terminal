import sys
import os
import datetime

args = sys.argv
directory = ""
file_name = ""

if "-d" in args:
    d_index = args.index("-d") + 1
    directories = []
    for arg in args[d_index:]:
        if arg == "-f":
            break
        directories.append(arg)
    directory = "/".join(directories)

    os.makedirs(directory, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f") + 1
    file_name = args[f_index]

    full_path = os.path.join(directory, file_name)

    with open(full_path, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        l_count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                f.write("\n")
                break
            f.write(str(l_count) + " " + line + "\n")
            l_count += 1
