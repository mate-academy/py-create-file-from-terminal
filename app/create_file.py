import sys
import os
from datetime import datetime


def get_directory_path() -> str:
    input_args = sys.argv
    path_parts = []
    if "-d" in input_args:
        start = input_args.index("-d") + 1
        for arg in input_args[start:]:
            if arg == "-f":
                break
            path_parts.append(arg)
    path = os.path.join(*path_parts) if path_parts else ""
    return path


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
    if not file_name:
        return
    full_file_path = os.path.join(path, file_name)
    is_file_exist = os.path.exists(full_file_path)
    with open(full_file_path, "a") as file:
        line_counter = 1
        file_content = ""
        while True:
            input_text = input("Enter content line: ")
            if input_text == "stop":
                break
            file_content += str(line_counter) + " " + input_text + "\n"
            line_counter += 1
        if file_content:
            if is_file_exist:
                file.write("\n\n")
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_content = current_time + "\n" + file_content
            file.write(file_content.strip())


directory_path = get_directory_path()
create_directories(directory_path)
create_file(directory_path)
