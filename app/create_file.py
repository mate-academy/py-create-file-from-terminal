import os
import sys
from datetime import datetime


data = sys.argv

path = ""
if "-d" in data:
    d_index = data.index("-d") + 1
    path_parts = []
    for part in data[d_index:]:
        if part.startswith("-"):
            break
        path_parts.append(part)
    if path_parts:
        path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)

if "-f" in data:
    f_index = data.index("-f") + 1
    filename = data[f_index]
    filepath = os.path.join(path, filename) if path else filename

    with open(filepath, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        counter = 1
        while True:
            text = input("Input text: ")

            if text.lower() == "stop":
                break

            file.write(f"{counter} {text}\n")
            counter += 1
