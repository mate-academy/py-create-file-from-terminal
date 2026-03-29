import argparse
import datetime
import os
import re


def terminal_to_file() -> None:
    parser = argparse.ArgumentParser(
        description="The app creates folders/files, "
                    "writes inside of those files"
    )
    parser.add_argument("-d",
                        nargs="+",
                        default=[],
                        help="-d dir1 dir2 "
                             "- creates directory dir1/dir2.")
    parser.add_argument("-f",
                        type=str,
                        default=None,
                        help="-f file.txt "
                             "- creates file.txt in current directory.")

    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        raise argparse.ArgumentError

    d_arguments_list, f_argument_str = args.d, args.f

    if d_arguments_list:
        create_folder(d_arguments_list)
    if f_argument_str:
        if not is_valid_filename(filename=f_argument_str):
            raise NameError("File is invalid")
        create_file(d_arguments_list, f_argument_str)


def create_folder(list_args_dir: list) -> None:
    universal_path = os.path.join(*list_args_dir)
    try:
        os.makedirs(universal_path, exist_ok=True)
    except OSError as e:
        raise OSError(f"{e}. Path is invalid, check "
                      f"for unaccepted symbols: '{universal_path}'")


def create_file(list_args_dir: list, file_name: str) -> None:
    if list_args_dir:
        universal_path = os.path.join(*list_args_dir)
    else:
        universal_path = ""

    universal_path = os.path.join(universal_path, file_name)

    if not os.path.exists(universal_path):
        writing_to_file(universal_path, "w")
    else:
        writing_to_file(universal_path, "a")


def writing_to_file(path: str, mode: str) -> None:
    user_input = accept_user_input()

    if len(user_input) < 2:
        return print("You cannot add an empty message")

    with open(path, mode) as file:
        file.writelines(datetime.date.strftime(datetime.datetime.now(),
                                               "%Y-%m-%d %H:%M:%S") + "\n")
        file.writelines(user_input)


def accept_user_input() -> list:
    full_message = list()

    while True:
        message = input("content line: ")
        if message == "stop":
            full_message.append("\n")
            break
        full_message.append(message + "\n")
    return full_message


def is_valid_filename(filename: str) -> bool:
    # re from Google
    return bool(re.match(r"^[\w.]+$", filename))


if __name__ == "__main__":
    terminal_to_file()
