import os
from datetime import datetime


def create_file_from_terminal(list_args: list) -> None:
    list_args = list_args[slice(1, len(list_args))]
    directories = []
    flags = False
    for arg in list_args:
        if str(arg).startswith("-"):
            if arg == "-d" or arg == "-f":
                flags = True
            else:
                raise Exception("Flag into args is incorrect")

        if (arg != "-d") and (arg != "-f") and flags:
            directories.append(arg)
    if len(directories) > 1:
        if not os.path.exists(os.path.join(*directories[: -1])):
            os.makedirs(os.path.join(*directories[: -1]))
    with open(os.path.join(*directories), "a") as out_file:
        time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        out_file.write(time + "\n")
        count = 1
        while True:
            value = input("Enter content line:")
            if value == "stop":
                break
            out_file.write(str(count) + " " + value + "\n")
            count += 1


if __name__ == "__main__":
    string_file = "app/create_file.py -f file.txt"
    string_dir_file = "app/create_file.py -d dir1 dir2 -f file.txt"

    create_file_from_terminal(string_file.split())
    print("-----")
    create_file_from_terminal(string_dir_file.split())
