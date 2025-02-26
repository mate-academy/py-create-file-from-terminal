import argparse
import os
from datetime import datetime


def create_dirs(dir_list: list) -> str:
    file_path = os.path.join(*dir_list)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    return file_path


parser = argparse.ArgumentParser()
parser.add_argument("-d", dest="dir_list", nargs="*", default=None)
parser.add_argument("-f", dest="file_name", nargs="*", default=None)
args = parser.parse_args()

created_dir = ""
if args.dir_list:
    created_dir = create_dirs(args.dir_list)

if args.file_name:
    with open(os.path.join(created_dir, args.file_name[0]), "a") as file:
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
