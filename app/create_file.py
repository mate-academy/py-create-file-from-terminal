import os
import datetime as dt
import sys


def make_dir(folder_names: list) -> None:
    path = "/".join(folder_names)
    os.makedirs(path, exist_ok=True)


def make_file(folder_names: list, file_name: str) -> None:
    if len(folder_names) > 0:
        path = "/".join(folder_names)
        path = path + "/"
    else:
        path = ""

    with open(f"{path}{file_name}", "a") as f:
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + "\n")
        line_num = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                f.write("\n")
                break
            line_num += 1
            f.write(f"{line_num} {content}\n")


def reading_initial_args() -> None:
    initial_args = sys.argv
    folder_names = []

    for ind, arg in enumerate(initial_args):
        if arg == "-d":
            for folder_name in initial_args[ind + 1:]:
                if folder_name == "-f":
                    break
                folder_names.append(folder_name)
            make_dir(folder_names)
        elif arg == "-f":
            file_name = initial_args[ind + 1]
            make_file(folder_names, file_name)


if __name__ == "__main__":
    reading_initial_args()
