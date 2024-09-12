import sys
import datetime
import os


def create_file(file_path: str) -> None:
    mode = "a" if os.path.isfile(file_path) else "w"
    with open(f"{file_path}", mode) as f:
        if mode == "a":
            f.write("\n")

        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_number = 1
        while True:
            next_line = input("Enter content line: ")
            if next_line == "stop":
                break
            f.write(f"{line_number} {next_line}\n")
            line_number += 1


def app_for_create_file() -> None:
    arg = sys.argv
    if "-d" in arg:
        dir_index = arg.index("-d") + 1
        file_index = arg.index("-f") if "-f" in arg else len(arg)
        directory = os.path.join(*arg[dir_index:file_index])
        os.makedirs(directory)
    else:
        directory = os.getcwd()

    if "-f" in arg:
        file_name = arg[arg.index("-f") + 1]
        create_file(os.path.join(directory, file_name))


if __name__ == "__main__":
    app_for_create_file()
