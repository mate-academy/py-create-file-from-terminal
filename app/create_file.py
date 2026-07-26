import sys
import os
from datetime import datetime


def create_file(file_path):
    with open(file_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S" + "\n"))
        in_put = input("Enter content line: ")
        while in_put != "stop":
            f.write(in_put + "\n")
            in_put = input("Enter content line: ")
        f.write("\n")


if "-d" in sys.argv and "-f" in sys.argv:
    os.makedirs("/".join(sys.argv[2:-2]))
    file_path = "/".join(sys.argv[2:-2]) + "/" + sys.argv[-1]
    create_file(file_path)
elif "-d" in sys.argv:
    os.makedirs("/".join(sys.argv[2:]))
elif "-f" in sys.argv:
    create_file(sys.argv[-1])
