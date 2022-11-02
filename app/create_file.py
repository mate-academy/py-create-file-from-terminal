import datetime
import os.path
import sys

current = datetime.datetime.now()
current_time = current.strftime("%Y-%m-%d %H:%M:%S")


def create_dir(index_d: int) -> str:
    path = ""
    for command in sys.argv[index_d:]:
        if command == "-f":
            break
        path = os.path.join(path, command)
        os.mkdir(path)
    return path


def create_file(index_f: int) -> None:
    with open(sys.argv[index_f], "a") as file:
        file.write(f"{current_time}\n")
        while True:
            text = input("Enter content line:") + "\n"
            if "stop" in text:
                break
            file.write(text)


def create_dir_and_file(index_d: int, index_f: int) -> None:
    path = create_dir(index_d)
    path = os.path.join(path, sys.argv[index_f])
    with open(path, "a") as file:
        file.write(f"{current_time}\n")
        while True:
            text = input("Enter content line:") + "\n"
            if "stop" in text:
                break
            file.write(text)


if "-d" and "-f" in sys.argv:
    index_file = sys.argv.index("-f") + 1
    index_dir = sys.argv.index("-d") + 1
    create_dir_and_file(index_dir, index_file)
elif "-d" in sys.argv:
    index_dir = sys.argv.index("-d") + 1
    create_dir(index_dir)
else:
    index_file = sys.argv.index("-f") + 1
    create_file(index_file)
