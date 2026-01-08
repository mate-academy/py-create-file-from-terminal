import sys
import os
from datetime import datetime


def get_directory_path() -> str:
    path = ""
    input_args = sys.argv
    if "-d" in input_args:
        start = input_args.index("-d") + 1
        for directory in input_args[start:]:
            if directory == "-f":
                break
            path += directory + "/"
    return path[:-1]


def create_directories(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except FileNotFoundError:
        return


def get_file_name() -> str:
    file_name = ""
    input_args = sys.argv
    if "-f" in input_args:
        file_name = input_args[input_args.index("-f") + 1]
    return file_name


def create_file(path: str) -> None:
    file_name = get_file_name()
    if file_name:
        full_file_path = path + "/" + file_name
        is_file_exist = os.path.exists(full_file_path)
        with open(full_file_path, "a") as f:
            line_counter = 1
            file_content = ""
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    break
                file_content += str(line_counter) + " " + input_text + "\n"
            if file_content:
                if is_file_exist:
                    f.write("\n\n")
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file_content = current_time + "\n" + file_content
                f.write(file_content.strip())
            f.close()


directory_path = get_directory_path()
create_directories(directory_path)
create_file(directory_path)
