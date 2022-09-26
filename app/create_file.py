import sys
import os
import datetime


def make_dir(path):
    path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def make_file(path="", file_name=""):
    with open(os.path.join(path, file_name), "a") as f:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{date}\n")
        count = 1
        while True:
            line = input("Enter line: ")
            if line == "stop":
                f.write("\n")
                break
            f.write(f"{count} {line}\n")
            count += 1


command = sys.argv[1:]
file_name = command[-1]
if "-f" in command and "-d" in command:
    path = make_dir(command[1:command.index("-f")])
    make_file(path, file_name)
elif "-d" in command:
    make_dir(command[1:])
else:
    make_file(file_name=file_name)
