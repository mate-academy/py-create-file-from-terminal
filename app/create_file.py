import os
import sys
from datetime import datetime


def create_path() -> str:
    current_dir = os.getcwd()
    cur_path = []
    for elem in sys.argv[2:]:
        if elem == "-f":
            break
        cur_path.append(elem)
    whole_path = os.path.join(current_dir, *cur_path)
    return whole_path


def create_file() -> None:
    current_dir = os.getcwd()
    file_name = ""
    for index, elem in enumerate(sys.argv[:]):
        if elem == "-f":
            file_name = sys.argv[index + 1]
    path_with_file = os.path.join(current_dir, file_name)
    page_number = 1
    with open(path_with_file, "a") as source_file:
        current_data = datetime.now()
        source_file.write(current_data.strftime("%Y-%m-%d %X\n"))
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            source_file.write(f"{page_number} {line_content}\n")
            page_number += 1


def create_file_with_command() -> None:
    if "-d" in sys.argv[1:] and "-f" in sys.argv[1:]:
        make_dir = create_path()
        os.makedirs(make_dir, exist_ok=True)
        os.chdir(make_dir)
        create_file()
    elif sys.argv[1] == "-d":
        make_dir = create_path()
        os.makedirs(make_dir, exist_ok=True)
    elif sys.argv[1] == "-f":
        create_file()


if __name__ == "__main__":
    create_file_with_command()
