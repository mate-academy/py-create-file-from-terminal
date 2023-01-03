import sys
import os
import datetime


output = sys.argv


def create_path(output: list) -> str:
    if output != "-d" or output != "-f":
        raise ValueError("Please write your command correctly!")
    for index in range(len(output)):
        if output[index] == "-d":
            path = ""
            for dir_index in range(index + 1, len(output)):
                if output[dir_index] == "-f":
                    break
                path += output[dir_index] + "/"
            return path


def create_dir(path: str) -> None:
    os.makedirs(path)


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


def main(output: list):
    if output[1] == "-d" and "-f" not in output:
        create_file(create_path(output))
    if output[-2] == "-f" and "-d" not in output:
        create_file(output[-1])
    if output[1] == "-d" or output[-2] == "-f":
        create_file(create_path(output) + output[-1])
