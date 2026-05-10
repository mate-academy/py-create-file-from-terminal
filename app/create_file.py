import os
import sys
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
path_parts = []
file_name = None

i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-d":
        i += 1
        while i < len(sys.argv) and not sys.argv[i].startswith("-"):
            path_parts.append(sys.argv[i])
            i += 1
        continue
    if arg == "-f":
        if i + 1 < len(sys.argv):
            file_name = sys.argv[i + 1]
            i += 2
        else:
            i += 1
            continue
    else:
        i += 1

if path_parts:
    target_dir = os.path.join(*path_parts)
    os.makedirs(target_dir, exist_ok=True)

if file_name:
    lines = []
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        lines.append(content)

    if path_parts:
        full_path = os.path.join(target_dir, file_name)
    else:
        full_path = file_name

    is_empty = not os.path.exists(full_path) or os.path.getsize(full_path) == 0

    with open(full_path, "a", encoding="utf-8") as f:
        if not is_empty:
            f.write("\n")

        f.write(timestamp + "\n")
        for number, text in enumerate(lines, start=1):
            f.write(f"{number} {text}\n")
