from datetime import datetime
import os
import sys


if "-d" in sys.argv:
    current_dir = os.getcwd()
    for i in range(2, len(sys.argv)):
        if sys.argv[i] == "-f":
            break
        os.makedirs(sys.argv[i])
        current_dir = os.path.join(current_dir, sys.argv[i])
        os.chdir(current_dir)
with open(sys.argv[-1], "a") as file:
    stroke = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = 1
    file.write(stroke)
    file.write("\n")
    while True:
        stroke = input("Enter content line: ")
        if stroke == "stop":
            break
        file.write(f"{line} {stroke}")
        file.write("\n")
        line += 1
