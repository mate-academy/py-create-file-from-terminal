import sys
import datetime
import os


def create_file(file_path: str) -> None:
    mode = "a" if os.path.isfile(file_path) else "w"
    with open(f"{file_path}", mode) as file:
        if mode == "a":
            print(mode)
            file.write("\n\n")

        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

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
    if "-d" in arg and "-f" in arg:
        dir_index = arg.index("-d") + 1
        file_index = arg.index("-f") \
            if arg.index("-d") < arg.index("-f") else len(arg)
        directory = os.path.join(*arg[dir_index:file_index])
        os.makedirs(directory)
        file_name = arg[arg.index("-f") + 1]
        create_file(os.path.join(directory, file_name))
    if "-d" in arg and "-f" not in arg:
        dir_index = arg.index("-d") + 1
        file_index = len(arg)
        directory = os.path.join(*arg[dir_index:file_index])
        os.makedirs(directory)
    if "-f" in arg and "-d" not in arg:
        file_name = arg[arg.index("-f") + 1]
        create_file(os.path.join(directory, file_name))


if __name__ == "__main__":
    app_for_create_file()
