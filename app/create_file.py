import sys
import os
from datetime import datetime


def write_file(path: str) -> None:
    with open(path, "a") as file:
        line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while line != "stop":
            file.write(line + "/n")
            line = input("Enter content line: ")
        file.write("/n")


def create_directory(route: list) -> None:
    path = os.path.join(*route)
    if not os.path.exists(path):
        os.makedirs(path)


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:

        if args.index("-d") < args.index("-f"):
            create_directory(args[1:-2])
            write_file(f"{os.path.join(*args[1:-2])}/{args[-1]}")
        else:
            create_directory(args[args.index("d") + 1:])
            write_file(f"{os.path.join(*args[args.index('-d') + 1:])}"
                       f"/{args[1]}")

    elif "-d" in args:
        create_directory(args[1::])

    elif "-f" in args:
        write_file(args[-1])


if __name__ == "__main__":
    main()
