import sys
import os
from datetime import datetime


def create_directories(args: list) -> str:
    dir_path = os.path.join(*args)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(f"{counter} {text}\n")
            counter += 1


def main() -> None:
    arg = sys.argv
    dir_path = None
    file_name = None
    file_path = None

    if "-d" in arg and len(arg) > 3:
        d_index = arg.index("-d")

        if "-f" in arg:
            f_index = arg.index("-f")
            dir_path = arg[d_index + 1:f_index]
            file_name = arg[f_index + 1]
        else:
            dir_path = arg[d_index + 1:]
    elif "-f" in arg and len(arg) > 3:
        f_index = arg.index("-f")
        file_name = arg[f_index + 1]

    if dir_path:
        full_path = create_directories(dir_path)
        if file_name:
            file_path = os.path.join(full_path, file_name)
    else:
        file_path = file_name

    if file_name:
        create_file(file_path)


if __name__ == "__main__":
    main()
