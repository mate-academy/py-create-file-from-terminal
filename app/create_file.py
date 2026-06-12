import datetime
import os
import sys

d_name = []
f_name = None

if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    f_name = sys.argv[f_index + 1]
    print (f_name)

if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    if "-f" in sys.argv and sys.argv.index("-f") > d_index:
        d_name = sys.argv[d_index + 1: sys.argv.index("-f")]
    else:
        d_name = sys.argv[d_index + 1:]
    print (d_name)

if f_name:
    if d_name:
        way_folders = os.path.join(*d_name)
        os.makedirs(way_folders, exist_ok=True)
        full_path = os.path.join(way_folders, f_name)
    else:
        full_path = f_name
    print("Final file path:", full_path)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(full_path, "a") as file:
        file.write(f"{timestamp}\n")
        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower().strip() == "stop":
                break
            file.write(f"{line_number} {user_input}\n")
            line_number += 1
else:
    print("Error: No file name specified due to flag -f")
