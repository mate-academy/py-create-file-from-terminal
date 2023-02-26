import sys
import os
from datetime import datetime


task = sys.argv[1:]


def create_file_and_content(name: str) -> None:
    with open(name, "a") as f:
        content = []
        content.append(datetime.now().strftime("%Y-%m-%d %X"))
        i = 1

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content.append(str(i) + " " + line)
            i += 1

        f.writelines(content)


if "-f" in task:
    if "-d" in task:
        path = os.path.join(*task[1:-2])
        os.makedirs(path)
    create_file_and_content(task[-1])
elif "-d" in task:
    path = os.path.join(*task[1:])
    os.makedirs(path)
