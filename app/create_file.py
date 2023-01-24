# write your code here
import datetime
import os.path
import sys
from os import makedirs, path


def create_new_dir(path_: str) -> None:
    if path_ is not None and not path.isdir(path_):
        makedirs(path_)


def normalise_and_validate(path_: list) -> None | str:
    norm_path = os.path.normpath(os.path.normcase(str(path_)))
    if len(norm_path) < 3 and ("-f" and "-d") not in norm_path:
        return
    return norm_path


def create_path(path_: str) -> str:
    name_file = []
    if "-d" in path_:
        if "-f" not in path_:
            list_dir = path_[path_.index("-d") + 1:]
        else:
            list_dir = path_[path_.index("-d") + 1:path_.index("-f")]
        path_ = os.path.join(*list_dir)
    if "-f" in path_:
        name_file = path_[path_.index("-f") + 1]
    full_path = os.path.join(path_, *name_file)
    return full_path


def write_file(path_: str) -> None:
    date_mark = datetime.datetime.now()
    with open(path_, "a") as new_file:
        new_file.write(f"{date_mark.strftime('%Y-%m-%d %H:%M:%S')}\n")
        number_line = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            new_file.write(f"{number_line} {new_line}\n")
            number_line += 1


def main() -> None:
    start_path_ = sys.argv
    norm_path = normalise_and_validate(start_path_)
    full_path = create_path(norm_path)
    create_new_dir(full_path)
    write_file(full_path)


if __name__ == "__main__":
    main()
