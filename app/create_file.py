import os
import sys
from datetime import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directories', nargs="*",
                    help="creates directories -d dir1 dir2")
parser.add_argument("-f", "--filename", default = "file.txt", required=True,
                    help="creates file -f filename")
args = parser.parse_args()
dir_path = "".join(sys.argv[0].split("/")[:-1])
if args.directories:
    for dir in args.directories:
        dir_path = os.path.join(dir_path, dir)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
file_path = os.path.join(dir_path, args.filename)


with open(file_path, "a") as file :
    line_index = 0
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    file.write("\n" + timestamp + "\n")
    while True:
        user_input = input("Enter content line or 'stop': ")
        if user_input == "stop":
            break
        line_index += 1
        file.writelines(f"{line_index} {user_input}\n")
