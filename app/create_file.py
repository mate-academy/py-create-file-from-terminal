from datetime import datetime
from argparse import ArgumentParser
import os


def create_dir(dir_path: str) -> str:
    path = ""
    for directory in dir_path:
        path = os.path.join(path, directory)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(dir_path: str, file_name: str) -> None:
    date_today = datetime.now()
    new_line = input("Enter new line of content: ")
    number_row = 0
    path = ""
    if dir_path:
        path = create_dir(dir_path)
    with open(os.path.join(path, file_name), "a") as file_out:
        file_out.write(f"{date_today.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while new_line != "stop":
            number_row += 1
            file_out.write(f"{number_row} Line{number_row} {new_line}\n")
            new_line = input("Enter new line of content: ")


def creating_from_terminal() -> None:
    parser = ArgumentParser()
    parser.add_argument("-f")
    parser.add_argument("-d", nargs="*")
    args = parser.parse_args()
    file_name = args.f
    directory_name = args.d

    if file_name and directory_name:
        create_file(directory_name, file_name)
    elif file_name:
        create_file(directory_name, file_name)
    elif directory_name:
        create_dir(directory_name)


def main() -> None:
    creating_from_terminal()


if __name__ == main():
    main()
