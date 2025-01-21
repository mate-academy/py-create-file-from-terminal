# write your code here
from datetime import datetime
import os.path
import sys


def create_folders(list_folders: list) -> str:
    path_folder = ""
    for dir_name in list_folders:
        path_folder = os.path.join(path_folder, dir_name)
        if os.path.exists(path_folder):
            continue
        os.mkdir(path_folder)
    return str(path_folder)


def write_to_file(files_name: str) -> None:
    with open(files_name, "a") as f:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        i = 0
        while True:
            current_line = input("Enter content line: ")
            if current_line == "stop":
                break
            current_line = f"{i + 1} {current_line}\n"
            f.write(current_line)
            i += 1


def check_argv(args: list) -> None:
    if (
            (len(args) < 3)
            or (args.count("-d") == 0 and args.count("-f") == 0)
            or (args.count("-d") > 1 or args.count("-f") > 1)
    ):
        raise ValueError(
            "It should be one flag -d or -f "
            "and at least one argument"
        )


if __name__ == "__main__":
    argv = sys.argv
    check_argv(argv)

    if argv.count("-d") == 1 and argv.count("-f") == 0:
        folders = argv[2:]
        ps = create_folders(folders)
    elif argv.count("-f") == 1 and argv.count("-d") == 0:
        file_name = argv[2]
        write_to_file(file_name)
    else:
        f_index = argv.index("-f")
        folders = argv[2:f_index]
        file_name = argv[f_index + 1]
        path_to_file = os.path.join(
            create_folders(folders),
            file_name
        )
        write_to_file(path_to_file)
