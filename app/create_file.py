import os
from datetime import datetime
import sys


if "-d" in sys.argv:
    dir_index = sys.argv.index("-d")
    file_index = sys.argv.index("-f")
    filepath = os.getcwd()
    new_dirs = sys.argv[dir_index + 1: file_index]
    new_dirs = os.path.join(*new_dirs)
    filepath = os.path.join(filepath, new_dirs)
    if not os.path.exists(filepath):
        os.makedirs(new_dirs)
        os.chdir(filepath)


if "-f" in sys.argv:
    with open(sys.argv[-1], "a+") as new_file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(time + "\n")
        while True:
            input_text = input("Enter content line: ")
            if input_text == "stop":
                break
            new_file.write(input_text + "\n")

for line in sys.stdin:
    if "q" == line.rstrip():
        break
    print(f"Input: {line}")

print("Exit")
