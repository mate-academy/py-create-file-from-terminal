import sys
import os
import datetime


def return_datetime() -> str:
    return f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def create_directories(dirs: list) -> str:
    path = os.path.join(os.getcwd(), *dirs)
    os.makedirs(path, exist_ok=True)
    return path


def create_and_write_text_to_file(file_path: str) -> None:
    with open(f"{file_path}", "a") as file:
        file.write(f"{return_datetime()}\n")
        sum_lines = 0
        while True:
            client_input = str(input("Enter content line: "))
            if client_input.strip().lower() == "stop":
                break
            else:
                sum_lines += 1
                file.write(f"{sum_lines} {client_input}\n")


def main() -> None:
    arguments = sys.argv[1:]
    dirs = []
    d_index = 0
    file_name = None
    if "-d" in arguments:
        d_index += arguments.index("-d")
        for i in range(d_index + 1, len(arguments)):
            if arguments[i + 1] == "-f":
                break
            else:
                dirs.append(arguments[i])
    if "-f" in arguments:
        f_index = arguments.index("-f")
        if f_index < len(arguments):
            file_name = arguments[f_index + 1]

    if dirs and file_name:
        dir_path = create_directories(dirs)
        file_path = os.path.join(dir_path, file_name)
        create_and_write_text_to_file(file_path)
    elif dirs:
        create_directories(dirs)
    elif file_name:
        file_path = os.path.join(os.getcwd(), file_name)
        create_and_write_text_to_file(file_path)
