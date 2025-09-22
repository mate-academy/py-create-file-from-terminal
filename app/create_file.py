import datetime
import sys
import os


args = sys.argv[1:]

dirs: list = []
file_name: str | None = None

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        if d_index < f_index:
            dirs = args[d_index + 1: f_index]
        else:
            dirs = args[d_index + 1:]
    else:
        dirs = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

if dirs:
    dir_path : str = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)
    if "-f" in args:
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = dir_path
else:
    file_path = file_name

if "-f" in args:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    with open(file_path, "a") as source_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(timestamp + "\n")

        for line_number, line in enumerate(lines, start=1):
            source_file.write(f"{line_number} {line}\n")

        source_file.write("\n")
