import sys
import os
from datetime import datetime


com_line = sys.argv
if "-d" in com_line:
    dirs = com_line[com_line.index("-d") + 1:]
    if "-f" in com_line:
        dirs = com_line[com_line.index("-d") + 1:com_line.index("-f")]
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
if "-f" in com_line:
    path = ""
    text = ""
    line = 1
    while True:
        content = input("Enter content line:")
        if content.lower() == "stop":
            break
        text += f"{line} {content}\n"
        line += 1
    with open(os.path.join(path, sys.argv[-1]), "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time}\n{text}")
