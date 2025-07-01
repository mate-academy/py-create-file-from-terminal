import sys
import os
import datetime

arg = sys.argv[1:]
directory_name = []
file_name = ""
marker_d = False
marker_f = False
for marker in arg:
    if marker == "-d":
        marker_d = True

    if marker == "-f":
        marker_f = True
        marker_d = False

    if marker_d is True and marker_f is False and marker != "-d":
        directory_name.append(marker)

    if marker_d is False and marker_f is True and marker != "-f":
        file_name += marker
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if directory_name:
    path = os.path.join(*directory_name)
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name)
    if os.path.exists(full_path):
        mode = "a"
    else:
        mode = "w"
    with open(full_path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n")
        f.write(timestamp + "\n")
        add_line = ""
        count = 1
        while True:
            add_line = input("Enter content line:")
            if add_line.lower() == "stop":
                break
            f.write(str(count) + " " + add_line + "\n")
            count += 1
else:
    if os.path.exists(file_name):
        mode = "a"
    else:
        mode = "w"
    with open(file_name, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n")
        f.write(timestamp + "\n")
        add_line = ""
        count = 1
        while True:
            add_line = input("Enter content line:")
            if add_line.lower() == "stop":
                break
            f.write(str(count) + " " + add_line + "\n")
            count += 1
