import os
from datetime import datetime
from sys import argv


def create_path(data):
    path = ""
    for directory in data:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
    return path


def open_file(file_name):
    with open(file_name, "a") as file_w:
        numeration = 1
        date = datetime.now()
        file_w.write(date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            content = input("Enter content line (type 'stop' to finish): ")
            if content == "stop":
                file_w.write("\n")
                break
            file_w.write(f"{numeration}" + content + "\n")
            numeration += 1


def operate_command() -> None:
    if "-d" in argv and "-f" in argv:
        path = create_path(argv[2:argv.index("-f")])
        file_name = argv[argv.index("-f") + 1]
        path = os.path.join(path, file_name)
        open_file(path)
    if argv[1] == "-d":
        create_path(argv[2:])
    elif argv[1] == "-f":
        open_file(argv[2])


if __name__ == "__main__":
    operate_command()
