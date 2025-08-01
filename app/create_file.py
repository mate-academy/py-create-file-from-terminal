import sys
from os import path, makedirs
from datetime import datetime


args = sys.argv[1:]


def parse_args(args: list) -> dict:
    result = {"-f": [], "-d": []}
    current_flag = None

    for arg in args:
        if arg in result:
            current_flag = arg
        elif current_flag:
            result[current_flag].append(arg)
    if not result["-f"]:
        result["-f"].append("file.txt")
    if not result["-d"]:
        result["-d"].append(".")
    return result


def create_file(args: list) -> None:
    flags_n_args = parse_args(args)
    dest = path.join(*flags_n_args["-d"])
    makedirs(dest, exist_ok=True)
    dest_file = path.join(dest, *flags_n_args["-f"])
    prompt = []
    _timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        prompt.append(user_input + "\n")

    with open(dest_file, "a") as fname:
        fname.write(_timestamp + "\n")
        fname.writelines(prompt)


create_file(args)


if __name__ == "main":
    pass
