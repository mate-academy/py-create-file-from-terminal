import os
import sys
from datetime import datetime


user_command = sys.argv[1:]
directory_path = []
file_name = ""

if "-d" in user_command:
    start_d = user_command.index("-d") + 1
    for i in range(start_d, len(user_command)):
        if user_command[i] == "-f":
            break
        directory_path.append(user_command[i])

if "-f" in user_command:
    idx_f = user_command.index("-f")
    if idx_f + 1 < len(user_command):
        file_name = user_command[idx_f + 1]

full_path = ""
if directory_path:
    full_path = os.path.join(*directory_path)
    os.makedirs(full_path, exist_ok=True)

if file_name:
    file_path = os.path.join(full_path, file_name)

    is_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a") as created_file:
        if is_not_empty:
            created_file.write("\n")

        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        created_file.write(date_time + "\n")

        line_num = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break

            created_file.write(f"{line_num} {user_input}\n")
            line_num += 1
