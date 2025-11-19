import sys
import os
import datetime

dirs = []
file_name = None

if "-d" in sys.argv:
    idx = sys.argv.index("-d")
    for arg in sys.argv[idx + 1:]:
        if arg.startswith("-"):
            break
        dirs.append(arg)

if "-f" in sys.argv:
    idx = sys.argv.index("-f")
    file_name = (sys.argv[idx + 1])

path = ""

if dirs:
    path = "/".join(dirs)
    os.makedirs(path, exist_ok=True)

if file_name:
    if path:
        file_path = f"{path}/{file_name}"
    else:
        file_path = f"{file_name}"

lines = []
while True:
    user = input("Enter content line:")
    if user == "stop":
        break
    lines.append(user)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_line = []
for index, word in enumerate(lines, start=1):
    new_line.append(f"{index} {word}")

block = timestamp + "\n" + "\n".join(new_line) + "\n"

with open(file_path, "a") as f:
    f.write(block)
    f.write("\n")
