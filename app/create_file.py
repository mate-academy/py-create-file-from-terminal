import datetime
import sys
import os


def create_file(file_path: str) -> None:
    mode = "a" if os.path.isfile(file_path) else "w"
    with open(f"{file_path}", mode) as file:
        if mode == "a":
            file.write("\n\n")

    file.write(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

    line_number = 1
    while True:
        next_line = input("Enter content line: ")
        if next_line == "stop":
            break
        file.write(f"\n{line_number} {next_line}")
        line_number += 1


def app_for_create_file() -> None:
    arg = sys.argv
    directory = os.getcwd()
    file_name = None

    if "-d" in arg:
        dir_index = arg.index("-d") + 1
        file_index = (
            arg.index("-f")
            if "-f" in arg and arg.index("-f") > arg.index("-d")
            else len(arg)
        )
        directory = os.path.join(*arg[dir_index:file_index])

    if "-f" in arg:
        file_name = arg[arg.index("-f") + 1]

    os.makedirs(directory, exist_ok=True)

    if file_name:
        create_file(os.path.join(directory, file_name))


if __name__ == "__main__":
    app_for_create_file()
