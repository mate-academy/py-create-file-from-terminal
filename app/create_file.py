import datetime

import sys

import os


os.chdir(
    "C:\\Users\\With my hand\\PycharmProjects\\"
    "py-create-file-from-terminal\\app"
)
current_dir = os.getcwd()
path = os.path.join(current_dir)


def create_dir(dir_name: str) -> None:
    try:
        os.makedirs(dir_name)
        os.chdir(dir_name)

    except FileExistsError:
        os.chdir(dir_name)


def check_file_exists(file_name: str) -> bool:
    file_path = os.path.join(os.getcwd(), file_name)
    return os.path.exists(file_path)


def create_file(file_name: str) -> None:
    check_exist = check_file_exists(file_name)
    with open(f"{file_name}", "a+") as file:
        if check_exist:
            file.write("\n\n")

        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        string_num = 1

        while True:
            input_line = input("Enter content line:")

            if input_line == "stop":
                return

            file.write(f"\n{string_num} {input_line}")
            string_num += 1


def find_commands(commands: list) -> None:
    for index in range(len(commands)):
        if commands[index] == "-d":
            continue

        if commands[index] == "-f":
            break
        create_dir(commands[index])
    create_file(commands[-1])


command = sys.argv[1:]
find_commands(command)
