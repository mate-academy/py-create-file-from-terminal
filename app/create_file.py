import sys
import os
from datetime import datetime


def create_dir(path: str) -> None:
    if os.path.exists(path):
        print("This directory already exists")
    else:
        os.makedirs(path)


def create_file(index_f: int, directory: str = "") -> None:
    file_name = sys.argv[index_f + 1]
    if directory:
        file_name = os.path.join(directory, file_name)
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_num = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(str(line_num) + " " + text + "\n")
            line_num += 1
        file.write("\n")


def main() -> None:
    input_data = sys.argv
    index_d = 0
    index_f = 0
    path = ""

    if len(input_data) < 2:
        print("Provide correct input")
        sys.exit(1)

    if "-d" in input_data:
        index_d = input_data.index("-d")
    if "-f" in input_data:
        index_f = input_data.index("-f")
    if index_f and index_d:
        for word in input_data[index_d + 1 : index_f]:
            path = os.path.join(path, word)
        create_dir(path)
        create_file(index_f, path)
    elif index_f:
        create_file(index_f)
    elif index_d:
        for word in input_data[index_d + 1:]:
            path = os.path.join(path, word)
        create_dir(path)


main()
