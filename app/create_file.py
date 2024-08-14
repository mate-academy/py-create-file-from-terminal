import os
import sys
from datetime import datetime


def create_dirs(d_path) -> None:
    os.makedirs(d_path, exist_ok=True)


def collect_data() -> str:
    info = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    counter = 1
    info.append(f"{current_time}\n")
    while True:
        line_from_user = input("Enter content line: ")
        if line_from_user == "stop":
            info.append("\n")
            break
        info.append(f"{counter} {line_from_user}\n")
        counter += 1
    return "".join(info)


def write_data(file: str, path: str = None) -> bool:
    file_path = os.path.join(path, file) if path else file
    data_from_user = collect_data()
    try:
        with open(file_path, "a") as file:
            file.write(data_from_user)
    except (PermissionError, OSError) as e:
        print(f"Cannot open/create file: {file}. Error {e}")
        return False
    else:
        return True


def parse_argv(arg: list) -> tuple | None:
    f_flag = None
    d_flag = None
    file_name = ""
    dir_path = ""
    if "-f" in arg:
        f_flag = True
        f_index = arg.index("-f")
    if "-d" in arg:
        d_flag = True
        d_index = arg.index("-d")
    if f_flag:
        if d_flag:
            dir_path = os.path.join(
                *arg[d_index + 1:f_index]
            ) if f_index > d_index else os.path.join(
                *arg[d_index + 1:]
            )
        file_name = arg[f_index + 1]
    else:
        if d_flag:
            dir_path = os.path.join(
                *arg[d_index + 1:]
            )
    return file_name, dir_path


def create_file() -> None:
    file, dirs = parse_argv(sys.argv[1:])
    if file:
        if dirs:
            create_dirs(dirs)
        is_success = write_data(file, dirs)
        if is_success:
            print("User data has written")
        else:
            print(f"Cannot create/write data in {file}")
    elif dirs:
        create_dirs(dirs)
        print("Directories have created")
    else:
        print("No f or d keys provided!")


if __name__ == "__main__":
    create_file()
