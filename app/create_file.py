import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    with open(path, "w") as f:
        actual_time = datetime.now()
        f.write(f"{actual_time.strftime('%Y-%m-%d %H:%M:%S')} \n")
        actual_line = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{actual_line} {line} \n")
            actual_line += 1


def create() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        os.makedirs(os.path.join(*sys.argv[2:]), exist_ok=True)
    if "-f" in sys.argv and "-d" not in sys.argv:
        create_directory(sys.argv[2])
    if "-d" in sys.argv and "-f" in sys.argv:
        directories = os.path.join(*sys.argv[2:sys.argv.index("-f")])
        os.makedirs(directories, exist_ok=True)
        create_directory(directories + sys.argv[-1])


if __name__ == "__main__":
    create()
