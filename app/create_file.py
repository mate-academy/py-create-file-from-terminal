import sys
import os
from datetime import datetime


def data_input(file_path: str) -> None:
    count = 0
    utc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "w") as file_time:
        file_time.write(utc_time + "\n")
        file_time.close()
    while True:
        count += 1
        text = input("Enter content line: ")
        if text.lower() == "stop":
            break

        with open(file_path, "a") as file:
            file.write(f"{count} {text} \n")


def only_d() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        d_index = sys.argv.index("-d")
        list_d = []
        list_d.extend(sys.argv[d_index + 1:])
        dir_path = os.path.join(list_d)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)


def only_f() -> None:
    if "-f" in sys.argv and "-d" not in sys.argv:
        f_index = sys.argv.index("-f")
        utc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(sys.argv[f_index + 1], "w") as file_time:
            file_time.write(utc_time + "\n")
            file_time.close()
        data_input(sys.argv[f_index + 1])


def with_d_and_f() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")

        list_d = []

        list_d.extend(sys.argv[d_index + 1:f_index])
        dir_path = os.path.join(*list_d)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, sys.argv[f_index + 1])

        data_input(file_path)


with_d_and_f()
only_d()
only_f()
