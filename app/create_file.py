import sys
import os
import datetime


args = sys.argv[1:]
directories = []
filename = None

if "-d" in args:
    index_d = args.index("-d")
    if "-f" in args:
        index_f = args.index("-f")
        directories = args[index_d + 1:index_f]
    else:
        directories = args[index_d + 1:]

if "-f" in args:
    index_f = args.index("-f")
    if index_f + 1 < len(args):
        filename = args[index_f + 1]

if len(directories) != 0:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    print(f"Directories created: {path}")

lines = []
while True:
    user_text = input("Enter content line: ")
    if user_text.lower() == "stop":
        break
    lines.append(user_text)

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if directories:
    file_path = os.path.join(*directories, filename)
else:
    file_path = filename

with open(file_path, "a") as file:
    file.write(current_time)
    for page_number, line in enumerate(lines, 1):
        file.write(f"{page_number + 1} {line}\n")
    file.write("\n")
