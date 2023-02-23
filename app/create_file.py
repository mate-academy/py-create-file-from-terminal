import sys
import os
from datetime import datetime


def main(commands: list) -> None:
    if "-d" in commands and "-f" not in commands:
        os.makedirs(os.path.join(*commands[1:]), exist_ok=True)
    elif "-f" in commands and "-d" not in commands:
        make_file(commands[-1])
    elif "-f" in commands and "-d" in commands:
        full_path = os.path.join(*commands[1:-2])
        file_name = commands[-1]
        os.makedirs(full_path, exist_ok=True)
        make_file(os.path.join(full_path, file_name))


def make_file(filename: str) -> None:
    user_data = [f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        user_data.append(f"{len(user_data)} {user_input}\n")

    with open(filename, "a+") as file:
        file.seek(0)
        data = file.read()
        if data:
            file.writelines(["\n"] + user_data)
        else:
            file.writelines(user_data)


if __name__ == "__main__":
    main(sys.argv[1:])
