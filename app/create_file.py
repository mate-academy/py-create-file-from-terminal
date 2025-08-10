# import argparse
import sys
import os
from datetime import datetime


def create_dirs(dir_list: list) -> str:
    file_path = os.path.join(*dir_list)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


dir_list = []
file_name = []
args = sys.argv[1:]
if "-f" in args:
    file_name = args[args.index("-f") + 1:]
    if "-d" in args:
        dir_list = args[args.index("-d") + 1:args.index("-f")]

# parser = argparse.ArgumentParser()
# parser.add_argument("-d", dest="dir_list", nargs="*", default=[])
# parser.add_argument("-f", dest="file_name", nargs=1, default=[])
# args = parser.parse_args()

created_dir = ""
if len(dir_list) > 0:
    created_dir = create_dirs(dir_list)

if len(file_name) > 0:
    with open(os.path.join(created_dir, file_name[0]), "a") as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        string_num = 0
        while True:
            new_string = input("Enter content line: ")
            if new_string == "stop":
                file.write("\n")
                break
            else:
                string_num += 1
                file.write(f"{string_num} {new_string}\n")
