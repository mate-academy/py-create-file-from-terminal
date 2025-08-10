import os
import sys
from datetime import datetime


def create_directory(path: list[str]) -> None:
    os.makedirs(os.path.join(*path), exist_ok=True)


def create_file(name: str) -> None:
    content = ""
    count = 0
    while True:
        count += 1
        line = input("Enter content line: ")
        if line == "stop":
            break
        content += "\n" + f"{count} " + line
    content += "\n\n"
    with open(name, "+a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.write(content)


def handle_command() -> None:
    args = sys.argv

    file_flag_index = args.index("-f") if "-f" in args else -1
    dir_flag_index = args.index("-d") if "-d" in args else -1
    file_name = args[file_flag_index + 1:][0]
    dir_path = (args[dir_flag_index + 1:file_flag_index]
                if file_flag_index > dir_flag_index
                else args[dir_flag_index + 1:])

    if dir_flag_index == -1:
        create_file(file_name)
    elif file_flag_index == -1:
        create_directory(dir_path)
    else:
        create_directory(dir_path)
        create_file(os.path.join(*dir_path, file_name))


if __name__ == "__main__":
    handle_command()
