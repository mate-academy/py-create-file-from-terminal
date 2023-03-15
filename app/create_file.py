import os
import sys
import datetime


def create_directories(directories: list) -> str:
    directories.remove("-d")
    if "-f" in directories:
        directories.remove("-f")
        os.makedirs(os.path.dirname(os.path.join(*directories)), exist_ok=True)
    else:
        os.makedirs(os.path.join(*directories), exist_ok=True)
    return os.path.join(*directories)


def create_file(source_file: str) -> None:
    current = datetime.datetime.now()
    with open(source_file, "a") as file:
        lines = ""
        num = 0
        file.write(f"{current.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while lines != "stop":
            lines = input("Enter content line:")
            num += 1
            if lines != "stop":
                file.write(f"{num} {lines}\n")
        file.write("\n")


sys.argv.remove(sys.argv[0])
if "-f" in sys.argv and "-d" in sys.argv:
    create_file(create_directories(sys.argv))
if "-f" in sys.argv:
    create_file(sys.argv[-1])
if "-d" in sys.argv:
    create_directories(sys.argv)
