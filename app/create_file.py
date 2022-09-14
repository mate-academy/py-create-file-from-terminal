import sys
import os
from datetime import datetime


list_command = sys.argv
if "-d" in list_command and "-f" not in list_command:
    args = list_command[2:]
    path_dir = os.path.join(*args)
    os.makedirs(path_dir)

if "-d" in list_command and "-f" in list_command:
    args = list_command[2:-2]
    path_dir = os.path.join(*args)
    os.makedirs(path_dir)
    path_file = list_command[-1:][-1]
    with open(f"{path_dir}/{path_file}", "w") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            data = input("Enter information: ")
            if data == "stop":
                break
            f.write(f"{data}\n")

if "-d" not in list_command and "-f" in list_command:
    path_file = list_command[-1:][-1]
    with open(f"{path_file}", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            data = input("Enter information: ")
            if data == "stop":
                break
            f.write(f"{data}\n")
