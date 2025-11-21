from datetime import datetime
import os
import sys


flags = sys.argv
new_arq = "file.txt"
new_dir = ""

if "-f" in flags:
    index = flags.index("-f")
    new_arq = flags[index + 1]
    flags.remove(flags[index])
    flags.remove(flags[index])

if "-d" in flags:
    index = flags.index("-d")
    dire = flags[index + 1:]
    for path in dire:
        new_dir = os.path.join(new_dir, path)
    os.makedirs(new_dir, exist_ok=True)
    new_dir = os.path.join(new_dir, new_arq)

with open(new_dir, "a") as file:
    time_now = datetime.now()
    file.write(time_now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    lines = 1
    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        file.write(f"{lines} {content_line}\n")
        lines += 1
