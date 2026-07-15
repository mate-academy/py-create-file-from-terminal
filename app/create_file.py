import sys
import os
from datetime import datetime

dir_parts = []
file_name = None

d_index = sys.argv.index("-d") if "-d" in sys.argv else None
f_index = sys.argv.index("-f") if "-f" in sys.argv else None

if d_index is not None:

    for arg in sys.argv[d_index + 1:]:
        if arg.startswith("-"):
            break
        dir_parts.append(arg)

if f_index is not None:
    file_name = sys.argv[f_index + 1]

if dir_parts:
    file_path = os.path.join(*dir_parts)
    os.makedirs(file_path, exist_ok=True)
else:
    file_path = ""

if file_name is not None:
    result_list = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        result_list.append(user_input)

    full_path = os.path.join(file_path, file_name)
    insert_blank_line = (
        os.path.exists(full_path)
        and os.path.getsize(full_path) > 0
    )

    with open(full_path, "a") as file:
        if insert_blank_line:
            file.write("\n")

        time_info = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(time_info + "\n")

        for index, line in enumerate(result_list, start=1):
            file.write(f"{index} {line}\n")
