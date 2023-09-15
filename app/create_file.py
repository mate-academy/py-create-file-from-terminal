import os
import sys
from datetime import datetime


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = os.path.join(
            *sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        )
        create_folder(path)
        create_file(path)
        return
    if "-d" in sys.argv:
        path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        create_folder(path)
    if "-f" in sys.argv:
        create_file()


def create_folder(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(path: str = os.getcwd()) -> None:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    if os.path.exists(file_name):
        with open(os.path.join(path, file_name), "a") as new_file:
            new_file.write("\n\n")
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    counter = 0
    while True:
        message = input("Enter content line: ")
        if message.lower() == "stop":
            break
        counter += 1
        content.append(f"{counter} {message}")
    with open(os.path.join(path, file_name), "a") as new_file:
        new_file.write("\n".join(content).rstrip())


if __name__ == "__main__":
    main()
