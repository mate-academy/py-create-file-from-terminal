import sys
import os
import datetime


folder_path = ""
file_name = ""

if "-d" in sys.argv:
    d_index = sys.argv.index("-d")

    if "-f" in sys.argv and sys.argv.index("-f") > d_index:
        f_index = sys.argv.index("-f")
        dir_names = sys.argv[d_index + 1 : f_index]
    else:
        dir_names = sys.argv[d_index + 1:]
    folder_path = os.path.join(*dir_names)

if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]

if folder_path:
    os.makedirs(folder_path, exist_ok=True)

full_file_path = os.path.join(folder_path, file_name)

if file_name:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    is_appended = (os.path.exists(full_file_path)
                   and os.path.getsize(full_file_path) > 0)

    with open(full_file_path, "a") as f:
        if is_appended:
            f.write("\n")
        f.write(now + "\n")
        for index, line in enumerate(lines, 1):
            f.write(f"{index} {line}\n")
