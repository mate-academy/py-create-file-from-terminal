import sys
import os
from datetime import datetime


def while_for_f(file_path: str) -> None:
    count = 0
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "w") as file_time:
        file_time.write(formatted_time + "\n")
        file_time.close()
    while True:
        count += 1
        text = input("write text here: ")
        if text == "stop":
            break

        with open(file_path, "a") as file:
            file.write(f"{count} {text} \n")


def with_d_and_f() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        ind_d = sys.argv.index("-d")
        ind_f = sys.argv.index("-f")

        list_d = []

        list_d.extend(sys.argv[ind_d + 1:ind_f])
        path_to_directory = os.path.join(*list_d)
        if path_to_directory:
            os.makedirs(path_to_directory, exist_ok=True)

        file_path = os.path.join(path_to_directory, sys.argv[ind_f + 1])

        while_for_f(file_path)


def only_d() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        ind_d = sys.argv.index("-d")
        list_d = []
        list_d.extend(sys.argv[ind_d + 1:])
        path_to_directory = os.path.join(list_d)
        if path_to_directory:
            os.makedirs(path_to_directory, exist_ok=True)


def only_f() -> None:
    if "-f" in sys.argv and "-d" not in sys.argv:

        ind_f = sys.argv.index("-f")

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(sys.argv[ind_f + 1], "w") as file_time:
            file_time.write(formatted_time + "\n")
            file_time.close()
        while_for_f(sys.argv[ind_f + 1])


with_d_and_f()
only_d()
only_f()
