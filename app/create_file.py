import argparse
import datetime
import os

parser = argparse.ArgumentParser(description="Create directories and files")
parser.add_argument("-f")
parser.add_argument("-d", nargs="+")
args = parser.parse_args()
if args.d:
    if len(args.d) > 1:
        os.makedirs(f"{args.d[0]}/{args.d[1]}")
    else:
        os.makedirs(args.d[0])
if args.f:
    count_string = 1
    if args.d:
        file_patch = os.path.join(args.d[0], args.d[1], args.f)
    else:
        file_patch = args.f
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
