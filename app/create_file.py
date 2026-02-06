import argparse
import os
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*")
    parser.add_argument("-f", nargs="?")
    args = parser.parse_args()

    directories = args.d if args.d else None
    file_name = args.f if args.f else None

    parent_dir = os.path.join(*directories) if directories else None
    if parent_dir:
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        if parent_dir and file_name:
            file_path = os.path.join(parent_dir, file_name)
        elif parent_dir:
            file_path = parent_dir
        elif file_name:
            file_path = file_name
        else:
            file_path = ""

        with open(file_path, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            while True:
                data = input("Enter content line:")
                if data.lower() == "stop":
                    break
                file.write(data + "\n")

    create_file()
