from datetime import datetime
import os
import sys


def file_content_printer(file_name: str) -> None:
    with open(file_name, "a") as file:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=file)
        counter = 1
        while True:
            line = input("Enter content line: ")
            if "stop" in line:
                break
            print(f"{counter} {line}", file=file)
            counter += 1


if "-d" in sys.argv and "-f" in sys.argv:
    path = os.path.join(*sys.argv[2:-2])
    os.makedirs(path)
    file_content_printer(f"{os.path.join(path, sys.argv[-1])}")
elif sys.argv[1] == "-d":
    os.makedirs(os.path.join(*sys.argv[2:]))
elif sys.argv[1] == "-f":
    file_content_printer(sys.argv[2])
