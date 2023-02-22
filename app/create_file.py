import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        with open(file_path, "a") as f:
            f.write("\n")
    else:
        with open(file_path, "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

    while True:
        line = input("Enter content line : ")
        if line == "stop":
            break
        with open(file_path, "a") as f:
            f.write(f"{line}\n")


if __name__ == "__main__":
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_path = os.path.join(*sys.argv[2:-1])
        file_name = sys.argv[-1]
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)
    elif "-d" in sys.argv:
        dir_path = os.path.join(*sys.argv[2:])
        os.makedirs(dir_path, exist_ok=True)
    elif "-f" in sys.argv:
        file_path = sys.argv[2]
        create_file(file_path)
