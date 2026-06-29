from datetime import datetime
import os
import sys
args = sys.argv

if "-d" in args:

    d_index = sys.argv.index("-d")
    directories = []

    for arg in args[d_index + 1:]:
        if arg.startswith("-"):
            break
        directories.append(arg)

    path = os.path.join(*directories)
    os.makedirs(path)

if "-f" in args:
    lines = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f_index = args.index("-f")
    name = args[f_index + 1]

    while True:

        user = input("Enter content line: ")

        if user == "stop":
            break
        lines.append(user)

    if "-d" in args:
        filepath = os.path.join(path, name)
    else:
        filepath = name

    file_exists = os.path.exists(filepath)

    with open(filepath, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(timestamp + "\n")

        for index, line in enumerate(lines, 1):
            file.write(f"{index} {line}\n")
