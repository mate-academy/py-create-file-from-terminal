import sys
import os
from datetime import datetime


def create_file(file_path: str = sys.argv[-1]) -> None:
    with open(file_path, "a") as s:
        s.write(str(datetime.now().strftime("%m-%d-%Y %H:%M:%S")) + "\n")
        while True:
            new = input("Enter content line: ")
            if new == "stop":
                break
            s.write(new + "\n")
        s.write("\n")


if "-d" in sys.argv and "-f" in sys.argv:
    os.makedirs("/".join(sys.argv[2:-2]))
    create_file("/".join(sys.argv[2:-2]) + "/" + sys.argv[-1])
elif "-f" in sys.argv:
    create_file(sys.argv[-1])
elif "-d" in sys.argv:
    os.makedirs("/".join(sys.argv[-2:]))
