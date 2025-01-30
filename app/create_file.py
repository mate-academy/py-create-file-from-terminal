import os
import sys
import datetime


args = sys.argv[1:]

if "-d" in args and "-f" not in args:
    args = args[1:]
    if len(args) > 0:
        path = os.path.join(*args)
        os.makedirs(path, exist_ok=True)

if "-f" in args and "-d" not in args:
    args = args[1:]
    if len(args) > 0:
        with open(f"{args[0]}", "a") as current_file:
            current_file.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + "\n")
            while True:
                current_line = input("Enter content line: ")
                if current_line == "stop":
                    break
                current_file.write(f"{current_line}\n")

if "-f" in args and "-d" in args:
    file_name = args.pop(-1)
    args = args[1:-1]
    if len(args) > 0:
        path = os.path.join(*args)
        os.makedirs(path, exist_ok=True)
        path = os.path.join(*args, file_name)
        with open(path, "a") as current_file:
            current_file.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + "\n")
            while True:
                current_line = input("Enter content line: ")
                if current_line == "stop":
                    break
                current_file.write(f"{current_line}\n")
