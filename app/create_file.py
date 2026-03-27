import sys
import os
import datetime
from typing import TextIO


def write_user_input(
        file_obj: TextIO,
        append: bool,
        index: int = 1
) -> None:
    if append:
        file_obj.write("\n\n")
    file_obj.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    while True:
        user_text = input("Enter content line:")
        if user_text == "stop":
            break
        file_obj.write("\n" + f"{index } {user_text}")
        index += 1


def write_to_file(cur_path: str, file_name: str) -> None:
    with open(os.path.join(cur_path, file_name), "a+") as file_to_write:
        file_to_write.seek(0)
        start = file_to_write.readlines()
        if start:
            file_to_write.seek(2)
            write_user_input(file_to_write, append=True)
        else:
            write_user_input(file_to_write, append=False)


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
    else:
        if "-f" in args:
            file_name = args[args.index("-f") + 1]
            write_to_file(cur_path, file_name)


if __name__ == "__main__":
    process_args()
