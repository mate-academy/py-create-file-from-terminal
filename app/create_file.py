import os
import sys
from datetime import datetime
from typing import Any


def create_directory(*args) -> Any:
    path_join = os.path.join(*args)
    os.makedirs(path_join, exist_ok=True)
    return path_join


def create_file(file_name: str, directory: str) -> None:
    if directory != "":

        if os.path.exists(directory):
            file_path = os.path.join(directory, file_name)

            with open(file_path, "w") as file:
                file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
                while True:

                    line = input("Enter content line: ")
                    if line == "stop":
                        break
                    file.write(line + "\n")
    else:
        with open(file_name, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            while True:

                line = input("Enter content line: ")
                if line == "stop":
                    break
                file.write(line + "\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            if d_index < f_index:
                path_join = create_directory(*args[d_index + 1:f_index])
            else:
                path_join = create_directory(*args[d_index + 1:])
            create_file(args[f_index + 1], path_join)
        else:
            create_directory(*args[d_index + 1:])

    elif "-f" in args:
        create_file(args[-1], "")


if __name__ == "__main__":
    main()
