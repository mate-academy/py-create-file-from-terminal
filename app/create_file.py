import sys
import os
import datetime

dir_path = ""
file_name = None


if "-d" in sys.argv:
    dir_index = sys.argv.index("-d") + 1
    if "-f" in sys.argv:
        end_index = sys.argv.index("-f")
    else:
        end_index = len(sys.argv)

    folders = sys.argv[dir_index:end_index]
    dir_path = os.path.join(*folders)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

if "-f" in sys.argv:
    file_index = sys.argv.index("-f") + 1
    file_name = sys.argv[file_index]

if file_name:
    if dir_path:
        full_path = os.path.join(dir_path, file_name)
    else:
        full_path = file_name

    file_exists = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    with open(full_path, "a") as f:
        if file_exists:
            f.write("\n")

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(now + "\n")

        line_num = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            f.write(f"{line_num} {content}\n")
            line_num += 1
