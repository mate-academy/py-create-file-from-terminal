import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(name: str) -> None:
    with open(name, "+a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write("\n" + line)
        f.write("\n\n")


command = " ".join(sys.argv)
if " -d " in command and " -f " not in command:
    path = os.path.join(*command.split("-d")[1].strip().split())
    create_directory(path)

if " -d " not in command and " -f " in command:
    name = command.split("-f")[1].strip()
    create_file(name)

if " -d " in command and " -f " in command:
    path = os.path.join(*command.split("-d")[1].split("-f")[0].strip().split())
    name = command.split("-f")[1].split()[0].strip()
    file_path = os.path.join(path, name)
    create_directory(path)
    create_file(file_path)
