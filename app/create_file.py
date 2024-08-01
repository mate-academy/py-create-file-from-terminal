import os
import sys
from datetime import datetime


def create_directories(args: list[str]) -> None:
    dir_path = os.path.join(*args)
    os.makedirs(dir_path, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as new_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(f"{timestamp}\n")
        counter = 1
        while True:
            text = input("Enter content line (or type stop to finish): ")
            if text.lower() == "stop":
                break
            else:
                new_file.write(f"{counter} {text}\n")
                counter += 1


def main() -> None:
    arg = sys.argv
    if "-d" in arg[:2]:
        d_index = arg.index("-d")
        if "-f" in arg:
            f_index = arg.index("-f")
            path_dir = arg[d_index + 1:f_index]
            create_directories(path_dir)
            path_file = arg[f_index + 1]
            create_file(path_file)
        else:
            path_dir = arg[d_index + 1:]
            create_directories(path_dir)
    elif "-f" in arg[:2]:
        f_index = arg.index("-f")
        if "-d" in arg:
            d_index = arg.index("-d")
            path_file = arg[f_index + 1]
            create_file(path_file)
            path_dir = arg[d_index + 1:]
            create_directories(path_dir)
        else:
            path_file = arg[f_index + 1]
            create_file(path_file)


if __name__ == "__main__":
    main()
