from datetime import datetime
import os
from sys import argv


def create_file() -> None:
    file_name = argv[argv.index("-f") + 1] if "-f" in argv else ""
    if file_name:
        argv.remove("-f")
        argv.remove(file_name)

    file_path = os.getcwd()
    if "-d" in argv:
        file_path = os.path.join(file_path, *argv[argv.index("-d") + 1:])
        create_change_dirs(file_path)

    if file_name:
        write_to_file(file_name, file_path)


def create_change_dirs(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)


def write_to_file(name: str, path: str) -> None:
    with open(name, "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_size = os.path.getsize(os.path.join(path, name))
        file.write(f"\n{time}\n") if file_size else file.write(f"{time}\n")
        i = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{str(i)} {text}\n")
            i += 1


if __name__ == "__main__":
    create_file()
