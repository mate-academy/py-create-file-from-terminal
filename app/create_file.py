import argparse
import os
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file_name")
parser.add_argument("-d", "--directories_to_create", nargs="+")

args = parser.parse_args()
current_path = os.getcwd()

if args.directories_to_create is not None:
    for folder in args.directories_to_create:
        try:
            os.mkdir(os.path.join(current_path, folder))
        except FileExistsError:
            pass
        current_path = os.path.join(current_path, folder)

if args.file_name is not None:
    with open(os.path.join(current_path, args.file_name), "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        line_count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                f.write("\n")
                break
            f.write(f"{line_count} {line} \n")
            line_count += 1
