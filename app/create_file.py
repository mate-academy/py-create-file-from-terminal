import os
import sys
from datetime import datetime


def create_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(str(datetime.now().
                       strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        line = 0
        while True:
            content = input("Enter content line: ")
            line += 1
            if content == "stop":
                break
            file.write(f"{line} " + content + "\n")
        file.write("\n")


def finding_path() -> None:
    cwd = sys.argv
    to_dir = ""

    if cwd[1] == "-d":
        if "-f" not in cwd:
            to_dir = os.path.join(*cwd[2:])

        os.makedirs(to_dir, exist_ok=True)

    if "-f" in cwd:
        to_file = os.path.join(to_dir, cwd[cwd.index("-f") + 1])
        create_file(to_file)


if __name__ == "__main__":
    finding_path()
