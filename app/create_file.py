import os
import datetime
import sys


def create_file(arguments: list) -> None:
    path = define_directories(arguments)
    make_directories(path)

    if "-f" in arguments:
        file_name = define_file_name(arguments)
        add_information_in_file(os.path.join(path, file_name))


def make_directories(taken_path: str) -> None:
    current_directory = os.getcwd()
    path = os.path.join(current_directory, taken_path)
    os.makedirs(path, exist_ok=True)


def define_file_name(arguments: list) -> str:
    index_f = arguments.index("-f")
    return " ".join(arguments[index_f + 1:index_f + 2])


def define_directories(arguments: list) -> str:
    if "-d" not in arguments:
        return ""
    index_d = arguments.index("-d")
    if "-f" in arguments:
        index_f = arguments.index("-f")
        if index_f < index_d:
            return os.path.join(*arguments[index_d + 1:])
        else:
            return os.path.join(*arguments[index_d + 1: index_f])
    return os.path.join(*arguments[arguments.index("-d") + 1:])


def add_information_in_file(file_name: str) -> None:
    lines_arr = []
    while True:
        new_string = input("Enter new line of content: ")
        if new_string != "stop":
            lines_arr.append(new_string)
        else:
            break

    no_file = False
    try:
        with open(file_name, "r") as file:
            pass
    except FileNotFoundError:
        no_file = "no file"
    with open(file_name, "a") as file:
        if no_file is False:
            file.write("\n" + "\n")
        current_time = datetime.datetime.now()
        file.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        if len(lines_arr) > 0:
            file.write("\n")
            for index, line in enumerate(lines_arr):
                if len(lines_arr) - 1 > index:
                    file.write(f"{index + 1} {line}\n")
                else:
                    file.write(f"{index + 1} {line}")


if __name__ == "__main__":
    create_file(sys.argv)
