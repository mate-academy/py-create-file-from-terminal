import sys
import os
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            f.write(content + "\n")


def create_dirs(parts_of_path: list[str]) -> None:
    path = os.path.join(*parts_of_path)
    os.makedirs(path, exist_ok=True)


def create_file_in_dirs(argv: list) -> None:
    parts_of_path = [part for part in argv if part not in ["-d", "-f"]]
    path = os.path.join(*parts_of_path)

    dir_path = os.path.dirname(path)
    os.makedirs(dir_path, exist_ok=True)

    with open(path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            f.write(content + "\n")


def main() -> None:
    try:
        flag1 = sys.argv[1]
        if flag1 == "-d" and "-f" not in sys.argv:
            create_dirs(sys.argv[2:])
        elif flag1 == "-f" and "-d" not in sys.argv:
            create_file(sys.argv[2])
        elif "-d" in sys.argv and "-f" in sys.argv:
            create_file_in_dirs(sys.argv[2:])
        else:
            print("Invalid arguments.")
    except IndexError:
        print("No arguments passed")


if __name__ == "__main__":
    main()
