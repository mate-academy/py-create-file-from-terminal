import sys
import os
from datetime import datetime


def create_dirs(dirs: list[str]) -> str:
    dir_path = os.path.join(*dirs)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = 1

        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line} Line{line} {user_input}" + "\n")

        file.write("\n")


def main() -> None:
    parameters = sys.argv[:]

    key_f = parameters.index("-f") if "-f" in parameters else None
    key_d = parameters.index("-d") if "-d" in parameters else None

    if key_f and not key_d:
        file_name = parameters[key_f + 1]
        create_file(file_name)

    elif key_d:
        if not key_f:
            dirs = parameters[key_d + 1:]
            create_dirs(dirs)

        else:
            dirs = (
                parameters[key_d + 1: key_f]
                if key_f > key_d
                else parameters[key_d + 1:]
            )
            path = os.path.join(create_dirs(dirs), parameters[key_f + 1])
            create_file(path)


if __name__ == "__main__":
    main()
