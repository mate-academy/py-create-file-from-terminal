import sys
import os
import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

command = sys.argv

if "-d" in command and "-f" not in command:
    d_index = command.index("-d")
    dir_parts = command[d_index + 1 :]
    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)

if "-f" in command and "-d" not in command:
    f_index = command.index("-f")
    file_name = "".join(command[f_index + 1 :])

    with open(file_name, "a") as f:
        f.write(f"{current_time}\n")
        counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{counter} {line}\n")
            counter += 1

if "-f" in command and "-d" in command:
    f_index = command.index("-f")
    file_name = "".join(command[f_index + 1 :])
    d_index = command.index("-d")
    parts = command[d_index + 1 : f_index]
    dir_path = os.path.join(*parts)
    dir_path_with_file = os.path.join(dir_path, file_name)
    os.makedirs(dir_path, exist_ok=True)

    with open(dir_path_with_file, "a") as f:
        f.write(f"{current_time}\n")
        counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{counter} {line}\n")
            counter += 1
        f.write("\n")
