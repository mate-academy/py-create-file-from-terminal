import os
import sys
import datetime


args = sys.argv
path_to_create_file = ""


if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args[d_index:].index("-f")
    else:
        f_index = len(args[d_index:])
    path_to_create_file = os.path.join(
        "",
        *args[d_index + 1:f_index + d_index]
    )
    os.makedirs(path_to_create_file, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")
    path_to_create_file = os.path.join(path_to_create_file, args[f_index + 1])
    with open(path_to_create_file, "a") as file:
        row = 1
        time = datetime.datetime.now()
        file.write("\n" + str(time.strftime("%Y-%m-%d %H:%M:%S")))
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"\n{row} {content}")
            row += 1
