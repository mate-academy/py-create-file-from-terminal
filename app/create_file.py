import sys
import os
from datetime import datetime


def create_new_file(path: str) -> None:
    with open(path, "a") as filename:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        filename.write(f"{formatted_time} \n")
        line_number = 1
        while True:
            info = input("Enter content line: ")
            if info == "stop":
                break
            filename.write(f"{line_number} {info} \n")
            line_number += 1
        filename.write("\n")


def create() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        os.makedirs(os.path.join(*sys.argv[2:]), exist_ok=True)
    elif "-f" in sys.argv and "-d" not in sys.argv:
        create_new_file(sys.argv[2])
    elif "-d" in sys.argv and "-f" in sys.argv:
        index_of_flag = sys.argv.index("-f")
        directories = os.path.join(*sys.argv[2:index_of_flag])
        os.makedirs(directories, exist_ok=True)
        create_new_file(directories + sys.argv[-1])


if __name__ == "__main__":
    create()
