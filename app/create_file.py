import os
import sys

from datetime import datetime


def create_file() -> None:
    dir_path = ""
    if "-d" in sys.argv:
        dir_path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name
        writing_in_file(file_path)


def writing_in_file(file_path: str) -> None:
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "w") as f:
        f.write(f"{time_now}\n")
        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                f.write("\n")
                break
            f.write(f"{line} {content}\n")
            line += 1


if __name__ == "__main__":
    create_file()
