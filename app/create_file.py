import sys
import os
import datetime


cmd_ls = sys.argv
parent_path = os.getcwd()
dir_path = ""

for _ in cmd_ls:
    if cmd_ls[1] == "-d" and cmd_ls[-2] == "-f":
        dir_path = "/".join(cmd_ls[2:-2])
        break
    elif cmd_ls[1] == "-d":
        dir_path = "/".join(cmd_ls[2:])
        break

path = os.path.join(parent_path, dir_path)
os.makedirs(name=path, exist_ok=True)

if cmd_ls[-2] == "-f":
    file_name = cmd_ls[-1]
    file_path = os.path.join(path, file_name)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{now}\n")
        content = input("Enter content line: ")
        i = 0
        while content != "stop":
            i += 1
            file.write(f"{i} {content}\n")
            content = input("Enter next content line: ")
        file.write("\n")
