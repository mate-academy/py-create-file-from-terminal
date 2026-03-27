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
    with open(f"{args.f[0]}", "a+") as file:
        file.write(f"{time_string}\n")
        count = 1
        while True:
            line = input(f"Enter content line: Line{count} content: ")
            if line == "stop":
                break
            file.write(f"{count} {line}\n")
            count += 1
        file.write("\n")


def create_dirs() -> None:
    os.makedirs(os.path.join(*args.d), exist_ok=True)


if args.f is None or args.d is not None:
    create_dirs()

if args.d is not None:
    os.chdir(os.path.join(*args.d))
if args.f is not None:
    create_file()
