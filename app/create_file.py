import time
import argparse
import os


named_tuple = time.localtime()
time_string = time.strftime("%m-%d-%Y, %H:%M:%S", named_tuple)
parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+", required=False)
parser.add_argument("-f", nargs="+", required=False)
args = parser.parse_args()


def create_file() -> None:
    with open(f"{args.f[0]}", "w") as file:
        pass
    with open(f"{args.f[0]}", "a+") as file:
        file.write(f"{time_string}\n")
    line = ""
    count = 1
    while line != "stop":
        line = input(f"Enter content line: Line{count} content")
        if line == "stop":
            break
        with open(f"{args.f[0]}", "a+") as file:
            file.write(f"{count} Line{count} content\n")
        count += 1


def create_dirs() -> None:
    os.makedirs(os.path.join(*args.d), exist_ok=True)


if args.f is None:
    create_dirs()
else:
    if args.d is None:
        create_file()
    else:
        create_dirs()
        os.chdir(os.path.join(*args.d))
        create_file()
