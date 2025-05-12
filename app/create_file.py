import os
import sys
from datetime import datetime

main_input_data = sys.argv
current_path = os.getcwd()

f_index = None
d_index = None
file_name = None
dir_list = None

if "-f" in main_input_data:
    f_index = main_input_data.index("-f")
    file_name = "".join(main_input_data[f_index + 1:])

if "-d" in main_input_data:
    d_index = main_input_data.index("-d") + 1
    dir_list = main_input_data[d_index:f_index]


def create_dir() -> str:
    try:
        if not dir_list:
            raise ValueError("No directories provided after '-d'.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    new_path = current_path
    for my_dir in dir_list:
        new_path = os.path.join(new_path, my_dir)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print(f"The path: '{new_path}' was created!")
    else:
        print("The path with such directories exist!")

    return new_path


def create_file(path: str = "") -> None:
    count = 1
    try:
        if not file_name:
            raise ValueError("No directories provided after '-f'.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    with open(os.path.join(path, file_name), "a") as file:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date_now}\n")
        while True:
            data = input("Enter content line: ")
            if data.lower() == "stop":
                break
            file.write(f"{count} {data}\n")
            count += 1


if "-d" in main_input_data and "-f" not in main_input_data:
    create_dir()

if "-f" in main_input_data and "-d" not in main_input_data:
    create_file()

if "-d" in main_input_data and "-f" in main_input_data:
    create_file(create_dir())
