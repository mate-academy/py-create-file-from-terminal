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
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "a") as file:
            file.write("\n")

    with open(f"{file_path}", "a") as file:
        file.write(f"{return_datetime()}\n")
        sum_lines = 0
        while True:
            client_input = str(input("Enter content line: "))
            if client_input.strip().lower() == "stop":
                break
            sum_lines += 1
            file.write(f"{sum_lines} {client_input}\n")


def main() -> None:
    arguments = sys.argv[1:]
    dirs = []
    file_name = None
    i = 0
    while i < len(arguments):
        argument = arguments[i]
        if argument == "-d":
            i += 1
            while i < len(arguments) and i != "-f":
                dirs.append(argument)
                i += 1
        elif argument == "-f":
            i += 1
            if i < len(arguments):
                file_name = argument
            else:
                print("The name of file should be written in")
        else:
            i += 1

    if dirs and file_name:
        dir_path = create_directories(dirs)
        file_path = os.path.join(dir_path, file_name)
        create_and_write_text_to_file(file_path)
    elif dirs:
        create_directories(dirs)
    elif file_name:
        file_path = os.path.join(os.getcwd(), file_name)
        create_and_write_text_to_file(file_path)
