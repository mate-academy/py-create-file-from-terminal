import sys
import os
from datetime import datetime


def name_folder(args: list) -> list:
    if "-d" in args and "-f" in args:
        index_d = args.index("-d")
        index_f = args.index("-f")
        return args[index_d + 1:index_f]
    elif "-d" in args:
        index_d = args.index("-d")
        return args[index_d + 1:]
    else:
        return []


def name_file(args: list) -> str:
    if "-f" in args:
        index_f = args.index("-f")
        return args[index_f + 1]
    else:
        return ""


command = sys.argv[1:]

folder_name = name_folder(command)
file_name = name_file(command)
if folder_name:
    os.makedirs(os.path.join(*folder_name), exist_ok=True)
    os.chdir(os.path.join(*folder_name))
if file_name:
    mode = "a" if os.path.exists(f"{file_name}.txt") else "w"
    count = 1
    with open(f"{file_name}.txt", mode) as output_file:
        output_file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        while True:
            content = sys.stdin.readline()
            if "stop" in content.lower():
                break
            stripped_content = content.strip()
            output_file.write(f"Line{count}: {stripped_content}\n")
            count += 1
