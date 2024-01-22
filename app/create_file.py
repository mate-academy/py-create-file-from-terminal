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

    if key_d:
        if key_f:
            if key_d < key_f:
                dirs = parameters[key_d + 1: key_f]
            else:
                dirs = parameters[key_d + 1:]
            path = os.path.join(create_dirs(dirs), parameters[key_f + 1])
            create_file(path)

        else:
            dirs = parameters[key_d + 1:]
            create_dirs(dirs)

    elif key_f:
        file_name = parameters[key_f + 1]
        create_file(file_name)


if __name__ == "__main__":
    main()
