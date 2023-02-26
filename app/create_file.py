import datetime
import os
import sys


def terminal() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        create_dir(sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")])
        create_file(sys.argv[-1])
        return
    if "-d" in sys.argv:
        create_dir(sys.argv[2:])
    if "-f" in sys.argv:
        create_file(sys.argv[-1])


def create_dir(path: list) -> None:
    os.makedirs(os.getcwd() + "\\" + "\\".join(path))


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        current_time = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S\n")
        file.write(current_time)

        count = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{count} {content}\n")
            count += 1


terminal()
