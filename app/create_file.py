import datetime
import os
import sys


def create_file(command: list, file_path: str) -> None:
    os.chdir(file_path)
    file_name = command[-1]
    with open(file_name, "a") as new_file:
        file_time = datetime.datetime.now().strftime("%Y-%M-%d %H:%M:%S")
        new_file.write(f"{file_time}\n")
        num_of_line = 1
        input_line = ""
        while input_line != "stop":
            input_line = input("Enter content line: ")
            if input_line != "stop":
                new_file.write(f"{num_of_line} {input_line}\n")
                num_of_line += 1


def create_dir(command: list) -> str:
    new_path = os.getcwd()
    for i in range(2, len(command)):
        if command[i] == "-f":
            break
        new_path = os.path.join(str(new_path), command[i])
    os.makedirs(new_path)
    return str(new_path)


def create_file_and_dir(comm_line: list) -> None:
    path = os.getcwd()
    if "-d" in comm_line:
        path = create_dir(comm_line)

    if "-f" in comm_line:
        create_file(comm_line, path)


create_file_and_dir(sys.argv)
