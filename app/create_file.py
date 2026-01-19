import sys
import os
import datetime


def start(command_line: list) -> None:
    if "-d" in command_line and "-f" in command_line:
        d_flag = command_line.index("-d")
        f_flag = command_line.index("-f")

        try:
            file_path = make_dir(command_line[d_flag + 1:f_flag])
        except FileExistsError as error:
            print(error)

        file_name = os.path.join(file_path, command_line[f_flag + 1])
        write_info(file_name)
        return

    if "-d" in command_line:
        d_flag = command_line.index("-d")

        try:
            make_dir(command_line[d_flag + 1:])
        except FileExistsError as error:
            print(error)

    if "-f" in command_line:
        f_flag = command_line.index("-f")
        write_info(command_line[f_flag + 1])


def make_dir(dir_path: list[str]) -> str:
    path = os.path.join(*dir_path)
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        raise FileExistsError("Directory already exists!")
    return path


def write_info(file_name: str) -> None:
    line = 1
    with open(file_name, "a") as f:
        current_time = datetime.datetime.now()
        f.write(current_time.strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            user_info = input("Enter content line: ")
            if user_info == "stop":
                f.write("\n")
                return
            f.write(f"{line} {user_info}\n")
            line += 1


start(sys.argv)
