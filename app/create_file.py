import sys
import os
from datetime import datetime


if "-d" in sys.argv:
    index = sys.argv.index("-d")
    dir_path = "/".join(sys.argv[index + 1:])
    os.makedirs(dir_path, exist_ok=True)

if "-f" in sys.argv:
    index = sys.argv.index("-f")
    file_name = sys.argv[index + 1]
    if "-d" in sys.argv:
        index = sys.argv.index("-d")
        dir_path = "/".join(sys.argv[index + 1:])
        file_path = f"{dir_path}/{file_name}"
    else:
        file_path = file_name
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"timestamp\n")

            i = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                file.write(f"{i} {content}\n")
                i += 1
    else:
        with open(file_path, "w") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"timestamp\n")

            i = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                file.write(f"{i} {content}\n")
                i += 1
