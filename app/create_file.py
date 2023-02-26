import os
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", nargs="+", help="directory path")
parser.add_argument("-f", "--file", help="file name")
args = parser.parse_args()

if args.directory:
    dir_path = os.path.join(*args.directory)
    os.makedirs(dir_path, exist_ok=True)

    if args.file:
        file_path = os.path.join(dir_path, args.file)
        with open(file_path, "a") as file:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(now + "\n")
            line_index = 1
            while True:
                line = input(f"Enter content line: {line_index} ")
                if line.lower() == "stop":
                    break
                file.write(f"{line_index} {line}\n")
                line_index += 1
            file.write("\n")

elif args.file:
    with open(args.file, "a") as file:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(now + "\n")
        line_index = 1
        while True:
            line = input(f"Enter content line: {line_index} ")
            if line.lower() == "stop":
                break
            file.write(f"{line_index} {line}\n")
            line_index += 1
        file.write("\n")

else:
    print("Error: Enter -d or -f flag.")
