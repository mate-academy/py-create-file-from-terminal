import datetime
import sys
import os


command = sys.argv
path = ""

def create_directory() -> None:
    path = ""
    for directory_name in command[2:]:
        if directory_name != "-f":
            path = os.path.join(path, directory_name)
        else:
            os.makedirs(path)
            create_and_write_to_file(path)
    os.makedirs(path)

def create_and_write_to_file(path: str) -> None:
    path = os.path.join(path, command[-1])
    with open(path, "a") as f:
        f.write(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            f.write(text + "\n")


if command[1] == "-d":
    create_directory()
elif command[1] == "-f":
    create_and_write_to_file(path)
