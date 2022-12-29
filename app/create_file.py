import os
import argparse
import datetime


parser = argparse.ArgumentParser(description="Create directories and files")
create_dir = parser.add_argument("-d", nargs="*")
create_file = parser.add_argument("-f", nargs=1)
args = parser.parse_args()

if args.d:
    path = os.path.join("app", *args.d)
    os.makedirs(path, exist_ok=True)

if args.f:
    new_file = ""

    if args.d and args.f:
        new_file = open(os.path.join("app", *args.d, *args.f), "a+")

    if args.d is None:
        new_file = open(os.path.join("app", *args.f), "a+")
    count = 0
    current_date = datetime.datetime.now()
    new_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S \n"))
    while True:
        input_string = input("Input content lines until you input stop: ")
        count += 1
        if input_string == "stop":
            break
        new_file.writelines(f"{count} {input_string}\n")

    new_file.close()
