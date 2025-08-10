import os
import sys
import datetime

argument_list = [arg for arg in sys.argv]


def create_directory(arguments: list) -> str:
    full_path = os.path.join(os.getcwd(), *arguments)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def create_file(name_of_file: str) -> None:
    with open(name_of_file, "a") as new_file:
        line_number = 1
        new_file.write(
            f"\n{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            new_file.write(f"{line_number} {line}\n")
            line_number += 1


def read_flags(arg_list: list) -> None:
    if "-d" in arg_list and "-f" in arg_list:

        if arg_list.index("-d") < arg_list.index("-f"):
            args = arg_list[arg_list.index("-d") + 1:arg_list.index("-f")]
            file_name = os.path.join(create_directory(args), arg_list[-1])

        else:
            args = arg_list[arg_list.index("-d") + 1::]
            file_name = os.path.join(
                create_directory(args),
                arg_list[arg_list.index("-f") + 1]
            )
        create_file(file_name)

    elif "-d" in arg_list:
        args = arg_list[arg_list.index("-d") + 1::]
        create_directory(args)

    elif "-f" in arg_list:
        file_name = os.path.join(os.getcwd(), arg_list[-1])
        create_file(file_name)


read_flags(argument_list)
