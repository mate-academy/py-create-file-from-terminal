import sys
import os
import datetime
from typing import TextIO


def write_user_input(counter: int, file_obj: TextIO) -> None:
    while True:
        user_text = input("Enter content line:")
        if user_text == "stop":
            break
        counter += 1
        file_obj.write(f"{counter } {user_text}" + "\n")


def write_to_file(cur_path: str, file_name: str) -> None:
    with open(os.path.join(cur_path, file_name), "a+") as file_to_write:
        file_to_write.seek(0)
        start = file_to_write.readlines()
        if start:
            start_counter = len(start) - 1
            write_user_input(start_counter, file_to_write)
        else:
            file_to_write.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )
            write_user_input(0, file_to_write)


def process_args() -> None:
    args = sys.argv
    cur_path = os.getcwd()
    if "-d" in args:
        if "-f" in args:
            dir_names = args[args.index("-d") + 1: args.index("-f")]
        else:
            dir_names = args[args.index("-d") + 1:]
        for folder in dir_names:
            if not os.path.isdir(os.path.join(cur_path, folder)):
                os.mkdir(os.path.join(cur_path, folder))
            cur_path = os.path.join(cur_path, folder)

        if "-f" in args:
            file_name = args[args.index("-f") + 1]
            write_to_file(cur_path, file_name)


if __name__ == "__main__":
    process_args()
