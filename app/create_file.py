import sys
import os
from datetime import datetime


def create_folder(folders: list[str]) -> str:
    path = os.path.join(*folders)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str) -> None:

    with open(file_name, "a") as file:
        file.write(datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = 1

        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line} {user_input}\n")
            line += 1


def main() -> None:
    args = sys.argv[:]

    flag_f = args.index("-f") if "-f" in args else None
    flag_d = args.index("-d") if "-d" in args else None

    if flag_d and flag_f:
        dirs = (
            args[flag_d + 1: flag_f]
            if flag_f > flag_d
            else args[flag_d + 1:]
        )
        path = os.path.join(create_folder(dirs), args[flag_f + 1])
        create_file(path)

    elif flag_f:
        file_name = args[flag_f + 1]
        create_file(file_name)

    else:
        dirs = args[flag_d + 1:]
        create_folder(dirs)


if __name__ == "__main__":
    main()
