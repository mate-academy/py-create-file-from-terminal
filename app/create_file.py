import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    return os.path.join(*directories)


def create_file() -> None:
    args = sys.argv
    base = os.getcwd()
    print(base)
    directories = []
    if "-d" in args:
        d_index = args.index("-d") + 1
        while d_index < len(args) and args[d_index] != "-f":
            directories.append(args[d_index])
            d_index += 1
        path_to_work_directory = create_path([base, *directories])
        os.makedirs(path_to_work_directory, exist_ok=True)
        base = path_to_work_directory

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        filepath = create_path([base, file_name])
        file_exist = os.path.isfile(filepath)

        with open(filepath, "a") as file:
            if file_exist:
                file.write("\n")
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{time}\n")
            count = 1
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                file.write(f"{count} {line}\n")
                count += 1


create_file()
