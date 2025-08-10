import datetime
import sys
import os

# write your code here

arguments = sys.argv

filename = arguments[-1]
dir_path = os.sep.join(arguments[arguments.index("-d") + 1
                                 if "-d" in arguments
                                 else len(arguments): arguments.index("-f")
                                 if "-f" in arguments
                                 else len(arguments)])


def create_dir_if_not_exists(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_user_input() -> str:
    user_input = []
    while True:
        input_line = input("Enter content line: ")
        if input_line == "stop":
            break
        user_input.append(input_line)
    return user_input


def get_current_formatted_datetime() -> datetime:
    return datetime.date.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")


def write_user_input_to_file(filename: str, dir_path: str = "") -> None:
    with open(os.path.join(dir_path, filename), "a") as file:
        file.write(f"{get_current_formatted_datetime()}\n")
        for index, input_line in enumerate(get_user_input()):
            file.write(f"{index + 1} {input_line}\n")


if "-d" in arguments and "-f" in arguments:
    create_dir_if_not_exists(dir_path)
    write_user_input_to_file(filename, dir_path)

elif "-f" in arguments:
    write_user_input_to_file(filename)


elif "-d" in arguments:
    create_dir_if_not_exists(dir_path)
