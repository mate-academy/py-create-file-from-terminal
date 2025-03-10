import os
import sys
import datetime
# python app/create_file.py -d dir1 dir2 -f file.txt


directory_index = -1
file_index = -1
directories = []
args = sys.argv
current_dir = os.getcwd()
file_name = ""
if "-d" in args:
    directory_index = args.index("-d")
if "-f" in args:
    file_index = args.index("-f")
if directory_index > 0:
    if file_index > 0:
        directories = args[directory_index + 1:file_index]
        file_name = args[file_index + 1]
        path = os.path.join(current_dir, *directories)
        os.makedirs(path)
        lines = []
        line_number = 0
        inp = ""
        while True:
            inp = input("Enter content line: ")
            if inp == "stop":
                break
            line_number += 1
            line = str(line_number) + " " + inp
            lines.append(line)

        with open(os.path.join(path, file_name), "w") as f:
            f.write(datetime.datetime.now().strftime("%Y-%M-%d %H:%m:%S"))
            for line in lines:
                f.write("\n" + line)
    else:
        directories = args[directory_index:]
        path = os.path.join(current_dir, *directories)
        os.makedirs(path)
