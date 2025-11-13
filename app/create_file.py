import datetime
import os
import sys

arguments = sys.argv


def create_directory(dirs: list[str]) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)  # не падає, якщо папка вже є


def create_file(name: str) -> None:
    datetime_line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(name, "a+") as file:
        file.write(datetime_line + "\n")
        line_counter = 1
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            file.write(f"{line_counter} {line}\n")
            line_counter += 1
        file.write("\n")


def check_args() -> None:
    if "-d" in arguments and "-f" in arguments:
        dirs = arguments[arguments.index("-d") + 1: arguments.index("-f")]
        create_directory(dirs)
        path_to_file = os.path.join(
            *dirs,
            arguments[arguments.index("-f") + 1]
        )
        create_file(path_to_file)
    elif "-d" in arguments:
        dirs = arguments[arguments.index("-d") + 1:]
        create_directory(dirs)
    elif "-f" in arguments:
        create_file(arguments[-1])


if __name__ == "__main__":
    check_args()
