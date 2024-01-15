import os.path
from sys import argv
from os import getcwd
from os import makedirs
import datetime
from datetime import datetime

length = len(argv)
command_line = []
root_dir = getcwd()
tail_dir = []
end_file = ""
full_path = ""


def body_function() -> None:
    make_command_line(length)
    print(f"The command line is: {command_line}")

    if "-d" in command_line and "-f" in command_line:
        both_flags()
    else:
        if length == 3 and command_line[1] == "-f":
            only_f_flag()

        if command_line[1] == "-d":
            only_d_flag()
            make_directories()


def make_command_line(argv_length: int) -> None:
    for _ in range(length):
        command_line.append(argv[_])
    print(f"The command line is: {command_line}")


def only_f_flag() -> None:
    global end_file
    end_file = command_line[2]
    make_file()


def only_d_flag() -> None:
    global tail_dir
    for _ in range(2, length):
        tail_dir.append(command_line[_])


def both_flags() -> None:
    global end_file
    global tail_dir

    end_file = command_line[length - 1]
    for _ in range(2, length - 2):
        tail_dir.append(command_line[_])

    make_directories()
    os.chdir(full_path)
    make_file()


def make_directories() -> None:
    global full_path
    full_path = root_dir
    for _ in tail_dir:
        full_path = os.path.join(str(full_path), _)
    if not os.path.exists(full_path):
        print(full_path)
        makedirs(full_path, 0o777)


def make_file() -> None:
    text_of_file = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n"
    counter = 1
    while True:
        line = input("Enter content line:")

        if line == "stop":
            text_of_file += "\n"
            break

        text_of_file += f"{str(counter)} {line}\n"
        counter += 1

    with open(end_file, "a+") as f:
        f.write(text_of_file)


body_function()
