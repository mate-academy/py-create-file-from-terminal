import sys
import os
import datetime


def creates_writ_file(file_name: str) -> None:
    if os.path.exists(file_name):
        writing_new_data_into_file(file_name, "a")
    else:
        writing_new_data_into_file(file_name, "w")


def writing_new_data_into_file(file_name: str,
                               parameter: str
                               ) -> None:
    with open(file_name, parameter) as source_file:
        source_file.write(datetime.datetime.now().
                          strftime("%Y-%m-%d %H:%M:%S") + "\n")
        number_string = 1
        while True:
            input_str = input("Enter content line: ")
            if input_str == "stop":
                break
            writing_str = str(number_string) + " " + input_str + "\n"
            number_string += 1
            source_file.write(writing_str)


def create_directory(path_elem: list) -> None:
    path = os.path.join(*path_elem)
    os.makedirs(path, exist_ok=True)


def read_string_args() -> None:
    len_sys_argv = len(sys.argv)

    if (sys.argv[1] == "-f"
            and "-d" not in sys.argv):
        creates_writ_file(sys.argv[2])

    if (sys.argv[1] == "-f"
            and "-d" in sys.argv):
        input_path = sys.argv[sys.argv.index("-d") + 1: len_sys_argv]
        create_directory(input_path)
        creates_writ_file(os.path.join(*input_path, sys.argv[2]))

    if (sys.argv[1] == "-d"
            and "-f" not in sys.argv):
        input_path = sys.argv[2: len_sys_argv]
        create_directory(input_path)

    if (sys.argv[1] == "-d"
            and "-f" in sys.argv):
        input_path = sys.argv[2: sys.argv.index("-f")]
        create_directory(input_path)
        creates_writ_file(os.path.join(*input_path, sys.argv[len_sys_argv]))


read_string_args()
