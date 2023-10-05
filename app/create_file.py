import argparse
import datetime
import os

parser = argparse.ArgumentParser(description="Create directories and files")
parser.add_argument("-f")
parser.add_argument("-d", nargs="*")
args = parser.parse_args()
if args.d:
    direction = os.path.join(*args.d)
    os.makedirs(direction, exist_ok=True)
if args.f:
    count_string = 1
    file_patch = os.path.join(*args.d, args.f) if args.d else args.f
    with open(file_patch, "a") as files:
        user_data = datetime.datetime.now()
        files.write(user_data.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            user_text = input("Enter content line:")
            if user_text != "stop":
                files.write(f"{count_string} {user_text}" + "\n")
                count_string += 1
            else:
                files.write("\n")
                break
