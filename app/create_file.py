import datetime
import os.path
import sys

current = datetime.datetime.now()
current_time = current.strftime("%Y-%m-%d %H:%M:%S")


def create_dir() -> str:
    path = ""
    for command in sys.argv[sys.argv.index("-d") + 1:]:
        if command == "-f":
            break
        path = os.path.join(path, command)
        os.mkdir(path)
    return path


def create_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(f"{current_time}\n")
        while True:
            text = input("Enter content line:") + "\n"
            if "stop" in text:
                break
            file.write(text)


def create_dir_and_file() -> None:
    path = create_dir()
    path = os.path.join(path, sys.argv[sys.argv.index("-f") + 1])
    create_file(path)


if __name__ == "__main__":
    if "-d" in sys.argv and "-f" in sys.argv:
        create_dir_and_file()
    if "-d" in sys.argv and "-f" not in sys.argv:
        create_dir()
    if "-f" in sys.argv and "-d" not in sys.argv:
        create_file(sys.argv[sys.argv.index("-f") + 1])
