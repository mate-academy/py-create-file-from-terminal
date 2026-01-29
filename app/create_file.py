import datetime
import sys
import os


command = sys.argv
path = ""
print(command)


def create_directory() -> None:
    for directory_name in command[2:]:
        if directory_name != "-f":
            path = os.path.join(path, directory_name)
            os.mkdir(path)
        else:
            create_directory(path)


def create_and_write_to_file(path: str) -> None:
    path = os.path.join(path, command[-1])
    with open(path, "a") as f:
        f.write(str(datetime.datetime.now()) + "\n")
        while True:
            text = input("Enter content line: ")
            if text != "stop":
                f.write(text + "\n")
            else:
                break


if command[1] == "-d":
    create_directory()
elif command[1] == "-f":
    create_and_write_to_file(path)
