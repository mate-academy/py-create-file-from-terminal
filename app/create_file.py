import os
from datetime import datetime
import sys


def create_directories_and_file() -> None:
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        if "-f" in sys.argv:
            file_index = sys.argv.index("-f")
            if dir_index < file_index:
                new_dirs_name = sys.argv[dir_index + 1: file_index]
            else:
                new_dirs_name = sys.argv[dir_index + 1:]
        else:
            new_dirs_name = sys.argv[dir_index + 1:]
        filepath = os.getcwd()
        new_dirs = os.path.join(*new_dirs_name)
        filepath = os.path.join(filepath, new_dirs)
        if not os.path.exists(filepath):
            os.makedirs(new_dirs, exist_ok=False)
            os.chdir(filepath)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        with open(sys.argv[file_index + 1], "a+") as new_file:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_file.write(time + "\n")
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    break
                new_file.write(input_text + "\n")


if __name__ == "__main__":
    create_directories_and_file()
