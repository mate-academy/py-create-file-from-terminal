import os
import sys
import datetime


def _create_dirs(args: list) -> str:
    try:
        flag_d_index = args.index("-d")
    except ValueError:
        return ""
    dirs = []
    for item in args[flag_d_index + 1:]:
        if item == "-f":
            break
        dirs.append(item)

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def _create_file(args: list, path: str) -> None:
    try:
        flag_f_index = args.index("-f")
    except ValueError:
        return
    file_name = args[flag_f_index + 1]
    file_name = os.path.join(path, file_name)

    if os.path.isfile(file_name):
        with open(file_name, "a") as current_file:
            current_file.write("\n")
            _fill_file(current_file)
    else:
        with open(file_name, "x") as current_file:
            _fill_file(current_file)


def _fill_file(current_file: open) -> None:
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_file.write(time + "\n")
    number_line = 1
    while True:
        data = input("Enter content line:")
        if data == "stop":
            break

        current_file.write(f"Line{number_line} " + data + "\n")
        number_line += 1


def create_file() -> None:
    args = sys.argv[1:]
    path = _create_dirs(args)
    _create_file(args, path)


if __name__ == "__main__":
    create_file()
