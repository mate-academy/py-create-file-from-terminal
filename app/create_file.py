from os import makedirs, path, chdir
from sys import argv

from datetime import datetime


def write_lines_to_file(
        arguments_list: list[str],
        file_flag: int
) -> None:
    paragraph_sign = ""

    with open(arguments_list[file_flag], "a") as write_file:

        with open(arguments_list[file_flag], "r") as read_file:
            if bool(read_file.readline()) is True:
                paragraph_sign = "\n"

        current_time = datetime.today().strftime("%Y-%d-%m %H:%M:%S")
        write_file.write(f"{paragraph_sign}{current_time}\n")
        counter = 1
        while True:
            input_text = input("Enter content line: ")
            if "stop" in input_text:
                break
            write_file.write(f"{counter} Line{counter} {input_text}\n")
            counter += 1


def create_directories(
        arguments_list: list[str],
        create_flag_index: int
) -> str:
    index_of_flag = arguments_list.index("-d")
    directory_str = path.join(
        "",
        *arguments_list[index_of_flag + 1:create_flag_index]
    )
    makedirs(directory_str, exist_ok=True)
    return directory_str


arguments = argv
if "-d" in arguments and "-f" in arguments:
    index_of_arg_create_flag = arguments.index("-f")
    directory = create_directories(arguments, index_of_arg_create_flag)
    chdir(directory)
    write_lines_to_file(arguments, index_of_arg_create_flag + 1)
elif "-d" in arguments:
    create_directories(arguments, len(arguments))
elif "-f" in arguments:
    index_of_arg_create_flag = arguments.index("-f")
    write_lines_to_file(arguments, index_of_arg_create_flag + 1)
