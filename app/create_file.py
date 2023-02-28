import sys
import os
from datetime import datetime


task = sys.argv[1:]


def create_file_and_content(name: str) -> None:
    with open(name, "a") as f:
        content = []
        content.append(datetime.now().strftime("%Y-%m-%d %X"))
        index = 1

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                content.append("\n")
                break
            content.append(str(index) + " " + line)
            index += 1

        f.writelines(content)


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


if "-f" in task:
    if "-d" in task:
        path = os.path.join(*task[1:-2])
        create_directory(path)
    create_file_and_content(task[-1])
elif "-d" in task:
    path = os.path.join(*task[1:])
    create_directory(path)
