import sys
import os
from datetime import datetime


argv = sys.argv[1::]


def create_folder(route: list) -> None:
    path_name = os.path.join(*route)
    if not os.path.exists(path_name):
        os.makedirs(path_name)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {text} \n")
            line_number += 1


if __name__ == "__main__":
    if "-d" in argv and "-f" in argv:
        if argv.index("-d") < argv.index("-f"):
            create_folder(argv[1:-2])
            create_file(f"{os.path.join(*argv[1:-2])}/{argv[-1]}")
        else:
            create_folder(argv[argv.index("-d") + 1:])
            create_file(f"{os.path.join(*argv[argv.index('-d') + 1:])}"
                        f"/{argv[1]}")
    elif "-d" in argv:
        create_folder(argv[1::])
    elif "-f" in argv:
        create_file(argv[-1])
