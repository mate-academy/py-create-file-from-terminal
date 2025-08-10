import datetime
import os
import sys


def terminal() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        os.makedirs(os.path.join(os.getcwd(), *path))
        create_file(os.path.join(*path, sys.argv[-1]))
    elif "-d" in sys.argv:
        os.makedirs(os.path.join(os.getcwd(), *sys.argv[2:]))
    elif "-f" in sys.argv:
        create_file(sys.argv[-1])


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
