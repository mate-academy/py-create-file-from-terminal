import datetime
from sys import argv
from os import makedirs, path


def datetime_in_format() -> str:
    data_time = datetime.datetime.today()
    return data_time.strftime("%Y-%m-%d %H:%M:%S")


def run_argv() -> None:
    data_terminal = argv

    if "-f" in data_terminal:
        index_f = data_terminal.index("-f")
        file_name = data_terminal[index_f + 1]
    else:
        index_f = len(data_terminal)
        file_name = None

    if "-d" in data_terminal:
        index_d = data_terminal.index("-d")
        if index_d < index_f:
            directory = data_terminal[index_d + 1:index_f]
        else:
            directory = data_terminal[index_d + 1:]
    else:

        directory = None

    if directory is not None:
        directory_join = path.join(*directory)
        makedirs(directory_join, exist_ok=True)

    if file_name is not None:
        print(file_name)
        if directory is not None:
            file_name = path.join(directory_join, file_name)
        with open(file_name, "a") as file_a:
            file_a.write(datetime_in_format() + "\n")
            count = 1
            input_msg = input("Enter content line: ")
            while input_msg != "stop":
                file_a.write(str(count) + " " + input_msg + "\n")
                count += 1
                input_msg = input("Enter content line: ")


run_argv()
