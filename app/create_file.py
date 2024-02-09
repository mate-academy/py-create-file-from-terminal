import os
import sys
from datetime import datetime


def create_file(name_of_file: str) -> None:
    with open(name_of_file, "a") as file:
        file_content = datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "\n"
        line_numbers = 0
        while True:
            line_numbers += 1
            user_input = input("Enter content line: ")
            if user_input == "stop":
                file_content += "\n"
                break
            file_content += f"{line_numbers} {user_input}\n"
        file.write(file_content)


def create_directory() -> str:
    dict_start_point = sys.argv.index("-d") + 1
    path = ""
    for element in range(dict_start_point, len(sys.argv)):
        if sys.argv[element] == "-f":
            break
        path = os.path.join(path, sys.argv[element])
    os.makedirs(path, exist_ok=True)
    return path


if "-d" in sys.argv and "-f" in sys.argv:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    directory_path = os.path.join(create_directory(), file_name)
    create_file(directory_path)
elif sys.argv[1] == "-d":
    create_directory()
elif sys.argv[1] == "-f":
    create_file(sys.argv[2])
