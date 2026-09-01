import sys
import os
import datetime


arguments = sys.argv


def find_flags(arguments: list[str]) -> None:
    index_f = None
    index_d = None
    for i in range(len(arguments)):
        if arguments[i] == "-f":
            index_f = i
        elif arguments[i] == "-d":
            index_d = i
    process_arguments(arguments, index_f, index_d)


def process_arguments(
        command: list[str],
        index_f: None | int,
        index_d: None | int
) -> None:

    if index_d is not None:
        end = len(command)

        if index_f is not None and index_f > index_d:
            end = index_f

        directories = command[index_d + 1: end]
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)

    if index_f is not None:
        file_name = command[index_f + 1]
        if index_d is not None:
            file_name = os.path.join(path, file_name)
        write_to_file(file_name)


def write_to_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        if os.path.getsize(file_name) > 0:
            f.write("\n")
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        count = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            count += 1
            f.write(f"{count} {line}\n")


find_flags(arguments)
