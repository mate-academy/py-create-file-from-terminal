import os
from _datetime import datetime


def file_creator_app(command: str) -> None:

    if "-d" in command and "-f" in command:
        directory_list = command.split("-f ")
        path_list = directory_list[0].split()
        path_list = path_list[3:]

        path_to_file = create_new_directory(path_list) + command.split()[-1]
        create_new_file(path_to_file)

    elif "-d" in command:
        directory_list = command.split("-d ")
        path_list = directory_list[-1].split()

        create_new_directory(path_list)

    elif "-f" in command:
        create_new_file(command)


def create_new_directory(path_list: list) -> str:
    path_ = ""
    for folder in path_list:
        path_ += folder + "/"
        if os.path.exists(path_) is not True:
            os.mkdir(path_)
    return path_


def create_new_file(command: str) -> None:
    if len(command) == 1:
        file_name = command
    else:
        file_name = command.split()[-1]
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as write_file:
        write_file.write("\n" + timestamp + "\n")
        while True:
            output = input("Enter content line:") + "\n"
            if output != "stop" + "\n":
                write_file.write(output)
            else:
                break
