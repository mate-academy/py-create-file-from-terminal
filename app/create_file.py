import os
import sys
import datetime

arguments = sys.argv
directory = []
filename = None

if "-d" in arguments:
    if "-f" in arguments:
        directory = arguments[arguments.index("-d") + 1:arguments.index("-f")]
    else:
        directory = arguments[arguments.index("-d") + 1:]
    if directory:
        os.makedirs(os.path.join(*directory), exist_ok=True)

if "-f" in arguments:
    filename = arguments[arguments.index("-f") + 1]
    if directory:
        filepath = os.path.join(*directory, filename)
    else:
        filepath = filename
    lines = []
    while True:
        line = input("Enter content line:")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    with open(filepath, "a") as output_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(f"{timestamp}\n")
        for line_number, line in enumerate(lines, start=1):
            output_file.write(f"{line_number} {line}\n")
