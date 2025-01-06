import sys
import os
import datetime


args = sys.argv[1:]
directory = os.getcwd()

if "-d" in args:
    d_index = args.index("-d")
    dirs = []
    for i in range(d_index + 1, len(args)):
        dirs.append(args[i])
    directory = os.path.join(directory, *dirs)
    os.makedirs(directory, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]
    file_path = os.path.join(directory, file_name)

    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"

    with open(file_path, mode) as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n"
        )
        if mode == "a":
            file.write("\n")

        line = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(f"{line} {text}\n")
            line += 1
