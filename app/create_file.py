import os
import sys
from datetime import datetime

main_input_data = sys.argv
current_path = os.getcwd()


def create_dir(input_data: list[str]) -> str:
    try:
        clean_list_dir = input_data[input_data.index("-d") + 1:]
        if not clean_list_dir:
            raise ValueError("No directories provided after '-d'.")
    except ValueError as e:
        print(e)
        sys.exit(1)

    new_path = current_path
    for my_dir in clean_list_dir:
        new_path = os.path.join(new_path, my_dir)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print(f"The path: '{new_path}' was created!")
    else:
        print("The path with such directories exist!")

    return new_path


def create_file(path: str = None) -> None:
    count = 1
    try:
        file_name = next(file for file in main_input_data if file.endswith(".txt"))
    except StopIteration:
        print("No file name after '-f'.")
        sys.exit(1)
    if path is not None:
        file_name = os.path.join(path, file_name)

    with open(file_name, "a") as file:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date_now}\n")
        while True:
            data = input("Enter content line: ")
            if data.lower() == "stop":
                break
            file.write(f"{count} {data}\n")
            count += 1


if "-d" in main_input_data and "-f" not in main_input_data:
    create_dir(main_input_data)

if "-f" in main_input_data and "-d" not in main_input_data:
    create_file()

if "-d" in main_input_data and "-f" in main_input_data:
    directories_without_file = main_input_data[:main_input_data.index("-f")]
    create_file(create_dir(directories_without_file))
