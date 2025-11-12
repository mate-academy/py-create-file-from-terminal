import os
import sys
import datetime


args = sys.argv[1:]
list_dirs = []
i = 0

while i < len(args):
    if args[i] == "-d":
        i += 1
        while i < len(args) and args[i] not in ("-d", "-f"):
            list_dirs.append(args[i])
            i += 1

    elif args[i] == "-f":
        if i + 1 < len(args):
            filename = args[i + 1]
            i += 2
        else:
            raise (Exception("No filename given"))
    else:
        i = i + 1

if list_dirs:
    path = os.path.join(*list_dirs)
    os.makedirs(path, exist_ok=True)
else:
    path = ""

full_path = os.path.join(path, filename)
lines = []
count = 1

while True:
    line = input("Enter content line: ")
    if line.lower() == "stop":
        break
    lines.append(f"{count} {line}")
    count += 1

current_date = datetime.datetime.now()
header = current_date.strftime("%Y-%m-%d %H:%M:%S")
body = "\n".join(lines)

if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
    prefix = "\n\n"
else:
    prefix = ""

final = prefix + header + "\n" + body + "\n"

with open(full_path, "a", encoding="utf-8") as f:
    f.write(final)
