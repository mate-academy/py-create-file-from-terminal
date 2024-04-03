import sys
import os
from datetime import datetime


def with_d_and_f() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        ind_d = sys.argv.index("-d")
        ind_f = sys.argv.index("-f")

        list_d = []

        list_d.extend(sys.argv[ind_d + 1:ind_f])
        str_list = "/".join(list_d)
        if not os.path.exists(str_list):
            os.makedirs(str_list)
        else:
            print("your directory alredy exist")

        file_path = os.path.join(str_list, sys.argv[ind_f + 1])
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


def only_d() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        ind_d = sys.argv.index("-d")
        list_d = []
        list_d.extend(sys.argv[ind_d + 1:])
        str_list = "/".join(list_d)
        if not os.path.exists(str_list):
            os.makedirs(str_list)
        else:
            print("your directory alredy exist")


def only_f() -> None:
    if "-f" in sys.argv and "-d" not in sys.argv:
        count = 0
        ind_f = sys.argv.index("-f")

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(sys.argv[ind_f + 1], "w") as file_time:
            file_time.write(formatted_time + "\n")
            file_time.close()

        while True:
            count += 1
            text = input("write text here: ")
            if text == "stop":
                break

            with open(sys.argv[ind_f + 1], "a") as file:
                file.write(f"{count} {text} \n")


with_d_and_f()
only_d()
only_f()
