import os
import sys
from datetime import datetime


def file_content_printer(current_file: str) -> None:
    with open(current_file, "a") as new_file:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=new_file)
        counter = 1
        while True:
            line = input("Enter content line: ")
            if "stop" in line:
                break
            print(f"{counter} {line}", file=new_file)
            counter += 1


def create_path(filename: str = None) -> str:
    dirs = filter(lambda x: "." not in x and x not in ["-f", "-d"], sys.argv)
    if filename and dirs:
        return os.path.join(*dirs, filename)
    if dirs:
        return os.path.join(*dirs)


def main() -> None:
    if "-f" in sys.argv and "-d" in sys.argv:
        file_name = filter(lambda x: "." in x, sys.argv[1:])
        os.makedirs(create_path(), exist_ok=True)
        file_content_printer(create_path(*file_name))
    elif sys.argv[1] == "-f":
        file_name = filter(lambda x: "." in x, sys.argv[1:])
        file_content_printer(*file_name)
    elif sys.argv[1] == "-d":
        os.makedirs(create_path(), exist_ok=True)


if __name__ == "__main__":
    main()
