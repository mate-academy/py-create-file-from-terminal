from datetime import datetime
from sys import argv
import os

commands = argv


def get_file() -> str:
    if "-f" in commands:
        return commands[-1]


def get_dirs() -> list[str]:
    if "-d" in commands:
        dirs = commands[commands.index("-d") + 1:commands.index("-f")]
        return dirs


def connect_path() -> str:
    dirs = os.path.join(*get_dirs()) if get_dirs() else os.getcwd()
    return os.path.join(dirs, get_file())


def get_data() -> list[str]:
    current_time = datetime.now()
    date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    input_list = [date_time + "\n"]
    i = 1
    while True:
        input_string = input("Enter content line: ")
        if input_string == "stop":
            break
        input_list.append(f"{i} {input_string}\n")
        i += 1
    input_list.append("\n")
    return input_list


def main() -> None:
    data = get_data()
    path = connect_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a" if os.path.exists(path) else "w") as f:
        f.writelines(data)


if __name__ == "__main__":
    main()
