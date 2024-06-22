import sys
import os
import datetime


def create_file(something: list[str]) -> None:
    dir_string = f"{os.getcwd()}\\"
    date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if "-d" in something:
        dir_string = directory_creation(something, dir_string)

    if "-f" in something:
        file_creation(something, dir_string, date)


def directory_creation(args_var: str, path: str) -> str:
    for i in range(args_var.index("-d") + 1, args_var.index("-f")):
        path = os.path.join(path, args_var[i])
        os.makedirs(path)
    return path


def file_creation(args_var: str, path: str, date: datetime) -> None:
    file_path = os.path.join(path,
                            args_var[args_var.index("-f") + 1])
    with open(file_path, "w") as f:
        flag = ""
        f.write(date + "\n")
        while True:
            flag = input("Enter content line (type 'stop' to finish): ")
            if flag == "stop":
                break
            f.write(flag + "\n")


create_file(sys.argv)
