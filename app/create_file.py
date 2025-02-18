import os
import datetime
import sys


def create_file(*args) -> None:
    arg_list = str(*args).split(" ")
    d_in_args = "-d" in arg_list
    f_in_args = "-f" in arg_list
    path = ""
    folders = []
    if d_in_args:
        d_arg_index = arg_list.index("-d")
        for i in range(d_arg_index + 1, len(arg_list)):
            if arg_list[i] == "-f":
                break
            folders.append(arg_list[i])
        path = create_path(folders)
        if not os.path.exists(path):
            os.makedirs(path)

    if f_in_args:
        f_arg_index = arg_list.index("-f")
        file_path = f"{path}{arg_list[f_arg_index + 1]}"
        mode = "w"
        if os.path.isfile(file_path):
            mode = "a"
        with open(file_path, mode) as file:
            if mode == "a":
                file.write("\n")
            line = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            file.write(f"{line}\n")
            line = ""
            lint = 1
            while True:
                line = input()
                if line == "stop":
                    break
                file.write(f"{line} {line}\n")
                lint += 1
        print(file_path)
    return None


def get_path(directories: list[str]) -> str:
    return str(os.path.join(*directories, ""))


def create_path(directories: list[str]) -> str:
    path = get_path(directories)
    return path


def main() -> None:
    create_file(sys.argv)


main()
