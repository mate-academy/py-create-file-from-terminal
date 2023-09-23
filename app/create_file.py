import os
import sys
from datetime import datetime


def create_dir(name_of_dir: list) -> str:

    path = os.path.join(*name_of_dir)
    os.makedirs(path, exist_ok=True)
    return path


def creat_file(file_name: str, path: str = os.getcwd()) -> None:
    with open(os.path.join(path, file_name), "a") as file:
        time_mark = datetime.now().strftime("%a %m %y %H:%M:%S")
        file.write(time_mark)
        while True:
            new_line = input("Enter content line: ")
            if new_line.lower() == "stop":
                break
            file.write(new_line)
        file.write("\n")


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = create_dir(sys.argv[sys.argv.index("-d") + 1:])
        file_name = sys.argv[sys.argv.index("-f") + 1]
        creat_file(file_name, path)
    elif "-d" in sys.argv:
        create_dir(sys.argv[sys.argv.index("-d") + 1:])

    elif "-f" in sys.argv:
        creat_file(sys.argv[sys.argv.index("-f") + 1])


if __name__ == "__main__":
    main()
