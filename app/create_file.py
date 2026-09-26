import os
import sys
import datetime


dir_parts = []
file_name = None

d_index = sys.argv.index("-d") + 1 if "-d" in sys.argv else None
f_index = sys.argv.index("-f") if "-f" in sys.argv else None

if d_index is not None:
    if f_index is not None and d_index < f_index:
        dir_parts = sys.argv[d_index:f_index]
    else:
        dir_parts = sys.argv[d_index:]

    if dir_parts:
        folder_path = os.path.join(*dir_parts)
        os.makedirs(folder_path, exist_ok=True)

if f_index is not None:
    file_name = sys.argv[f_index + 1]

    if dir_parts:
        file_path = os.path.join(*dir_parts, file_name)
    else:
        file_path = file_name

    content = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        else:
            content.append(line)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists_and_not_empty = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )
    with open(file_path, "a") as f:
        if file_exists_and_not_empty:
            f.write("\n")
        f.write(f"{timestamp}\n")
        for index, line in enumerate(content, start=1):
            f.write(f"{index} {line}\n")
