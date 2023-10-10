import datetime
import os
import sys


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                   + "\n")
        i = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{i} {line}\n")
            i += 1


def create_dirs(dirs: list) -> None:
    os.makedirs(os.path.join(*dirs), exist_ok=True)


def read_line() -> None:
    line_args = sys.argv
    path = []
    if "-d" in line_args:
        for directory in line_args[line_args.index("-d") + 1:]:
            if directory != "-f":
                path.append(directory)
            else:
                break
        create_dirs(path)
    if "-f" in line_args:
        file_name = line_args[line_args.index("-f") + 1]
        if path:
            file_path = os.path.join(*path, file_name)
        else:
            file_path = os.path.join(file_name)
        create_file(file_path)


if __name__ == "__main__":
    read_line()
