import sys
import os
import datetime


OUTPUT = sys.argv


def create_path(sys_output: list) -> str:
    for index in range(len(sys_output)):
        if sys_output[index] == "-d":
            path = ""
            for dir_index in range(index + 1, len(sys_output)):
                if sys_output[dir_index] == "-f":
                    break
                path += sys_output[dir_index] + "/"
            return path


def create_file(name: str) -> None:
    with open(f"{name}", "a") as new_file:
        new_file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        number = 0
        while True:
            number += 1
            some_input = input("Enter content line: ")
            if some_input == "stop":
                new_file.write(" \n")
                break
            new_file.write(f"{number} {some_input}\n")


if OUTPUT[1] == "-d" and "-r" not in OUTPUT:
    os.makedirs(create_path(OUTPUT))


if OUTPUT[-2] == "-f" and "-d" not in OUTPUT:
    create_file(OUTPUT[-1])

if OUTPUT[1] != "-d" or OUTPUT[-2] != "-f":
    raise ValueError("Please write your command correctly!")

if OUTPUT[1] == "-d" or OUTPUT[-2] == "-f":
    create_file(create_path(OUTPUT) + OUTPUT[-1])
