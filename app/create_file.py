import os
import sys
from datetime import datetime
import argparse


def get_command_from_terminal() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directories", nargs="*",
                        help="creates directories -d dir1 dir2")
    parser.add_argument("-f", "--filename", default="file.txt", required=True,
                        help="creates file -f filename")
    args = parser.parse_args()
    directories = args.directories
    filename = args.filename
    return directories, filename


def file_manager() -> str:
    dir_names, file_name = get_command_from_terminal()
    dir_path = "".join(sys.argv[0].split("/")[:-1])
    if dir_names:
        for directory in dir_names:
            dir_path = os.path.join(dir_path, directory)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
    file_path = os.path.join(dir_path, file_name)
    return file_path


def getting_timestamp() -> str:
    timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def writing_to_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        line_index = 0
        file.write("\n" + getting_timestamp() + "\n")
        while True:
            user_input = input("Enter content line or 'stop': ")
            if user_input == "stop":
                break
            line_index += 1
            file.writelines(f"{line_index} {user_input}\n")


if __name__ == "__main__":
    filepath = file_manager()
    writing_to_file(filepath)
