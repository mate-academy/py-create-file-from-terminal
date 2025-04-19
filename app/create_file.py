import sys
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
            if "stop" == input_text:
                break
            write_file.write(f"{counter} Line{counter} {input_text}\n")
            counter += 1


def create_directories(
        arguments_list: list[str],
        directory_index: int,
        file_index: int
) -> str:
    directory_str = path.join(
        "",
        *arguments_list[directory_index + 1:file_index]
    )
    makedirs(directory_str, exist_ok=True)
    return directory_str


def verify_arguments(
        arguments_list: list[str],
        directory_index: int,
        file_index: int
) -> None:
    if file_index == len(arguments_list) - 1:
        sys.exit("There should be at least one argument after flag -f!")
    if directory_index + 1 - file_index == 0:
        sys.exit("There should be at least one argument after flag -d!")
    if file_index < directory_index:
        sys.exit("Incorrect order of flags. Please make order as follows: -d args -f args")


def verify_single_argument(
        arguments_list: list[str],
        index: int
) -> None:
    if index == len(arguments_list) - 1:
        sys.exit("There should be at least one argument after the flag!")
    if arguments_list[index] in arguments_list[index + 1:]:
        sys.exit("Duplicate flag detected. Please make sure you're using only one instance of the flag.")


arguments = argv
if "-d" in arguments and "-f" in arguments:
    index_of_arg_create_flag = arguments.index("-f")
    directory_index = arguments.index("-d")

    verify_arguments(arguments, directory_index, index_of_arg_create_flag)
    directory = create_directories(arguments, directory_index, index_of_arg_create_flag)
    chdir(directory)
    write_lines_to_file(arguments, index_of_arg_create_flag + 1)

elif "-d" in arguments:
    directory_index = arguments.index("-d")

    verify_single_argument(arguments, directory_index)
    create_directories(arguments, directory_index, len(arguments))

elif "-f" in arguments:
    index_of_arg_create_flag = arguments.index("-f")
    verify_single_argument(arguments, index_of_arg_create_flag)
    write_lines_to_file(arguments, index_of_arg_create_flag + 1)

else:
    sys.exit("No flags or arguments provided. Please add -d, -f or both after file name. "
          "Expected format: -d dir1 dir2 -f filename")
