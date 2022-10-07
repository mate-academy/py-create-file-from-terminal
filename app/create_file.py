import os.path
import sys
from datetime import datetime


def get_from_terminal() -> None:
    path_or_name = sys.argv[1:]

    path = "."

    if "-d" in path_or_name:
        path_start = path_or_name.index("-d") + 1
        path_end = (
            path_or_name.index("-f")
            if "-f" in path_or_name
            else len(path_or_name)
        )
        path = "/".join(path_or_name[path_start:path_end])
        make_dir(path)

    if "-f" in path_or_name:
        file_name = path_or_name[path_or_name.index("-f") + 1]
        make_file(path + "/" + file_name)


def make_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def make_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_counter = 0

        while True:
            user_input = input("Enter content line: ")

            if user_input == "stop":
                file.write("\n")
                break

            line_counter += 1
            file.write(f"{line_counter} {user_input}\n")


if __name__ == "__main__":
    get_from_terminal()
