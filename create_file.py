import sys
import os
from datetime import datetime

count = 0
home_directory = sys.argv
if "-d" in home_directory:
    if "-f" in home_directory:
        path = os.path.join("\\".join(home_directory[home_directory.index("-d") + 1:home_directory.index("-f")]))
    else:
        path = os.path.join(
            "\\".join(
                home_directory[home_directory.index("-d") + 1::]
            )
        )
    os.makedirs(path)

if "-f" in home_directory:
    if "-d" in home_directory:
        path = os.path.join(
            path, home_directory[home_directory.index("-f") + 1]
        )
    else:
        path = home_directory[home_directory.index("-f") + 1]

    with open(path, "w") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            count += 1
            word = input("Enter content line:")
            if word == "stop":
                break
            file.write(f"{count} {word}\n")
