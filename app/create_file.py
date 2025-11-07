import os
import sys
from datetime import datetime


args = sys.argv


def create_file(path: str) -> None:
    with open(path, "a") as file:
        if file.tell() > 0:
            file.write("\n")

        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{now_time}\n")

        counter = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break

            file.write(f"{counter} {text}\n")
            counter += 1


if len(args) < 2:
    print("Error: No flags provided (-d or -f).")
    sys.exit(1)

if args[1] == "-d":
    dirs = []
    i = 2
    while i < len(args) and args[i] != "-f":
        dirs.append(args[i])
        i += 1

    dir_path = os.path.join(os.getcwd(), *dirs)
    os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_idx = args.index("-f")
        if f_idx + 1 >= len(args):
            print("Error: Filename is missing after -f.")
            sys.exit(1)
        filename = args[f_idx + 1]
        path = os.path.join(dir_path, filename)
        create_file(path)


if args[1] == "-f":
    if len(args) < 3:
        print("Error: Filename is missing after -f.")
        sys.exit(1)
    filename = args[2]
    path = os.path.join(os.getcwd(), filename)
    create_file(path)
