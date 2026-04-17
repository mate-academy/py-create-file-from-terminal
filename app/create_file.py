import sys
import os
import datetime


path = None

if "-d" in sys.argv:
    # directories = sys.argv[sys.argv.index("-d") + 1:]
    if "-f" in sys.argv:
        directories = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
    else:
        directories = sys.argv[sys.argv.index("-d") + 1:]

    if directories:
        path = os.path.join(*directories)
        os.makedirs(path)

if "-f" in sys.argv:
    lines = []
    file_name = sys.argv[sys.argv.index("-f") + 1]
    if path is not None:
        full_path = os.path.join(path, file_name)
    else:
        full_path = file_name
    with open(full_path, "a") as f:
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line_number, line in enumerate(lines, 1):
            f.write(f"{line_number} {line}\n")
        f.write("\n")
