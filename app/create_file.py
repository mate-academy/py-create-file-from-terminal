import sys
import os
import datetime
from typing import List


def find_file_name(args: List[str]) -> str:
    for index, arg in enumerate(args):
        if arg == "-f":
            return args[index + 1]

    return ""


def create_directories(args: List[str]) -> str:
    path = ""

    try:
        dir_index = args.index("-d")
    except ValueError:
        return path

    for i in range(dir_index + 1, len(args)):
        if args[i] == "-f":
            break

        path = os.path.join(path, args[i])

    os.makedirs(path, exist_ok=True)

    return path


def handle_input() -> List[str]:
    inputs_to_file = []

    while True:
        input_text = input("Enter content line: ")

        if input_text == "stop":
            break

        inputs_to_file.append(input_text)

    return inputs_to_file


def append_to_file(
    path: str,
    file_name: str,
    inputs: List[str]
) -> None:
    file_path = os.path.join(path, file_name)

    file_existed = os.path.isfile(file_path)

    with open(file_path, "a") as file:
        if file_existed:
            file.write("\n")

        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n"
        )

        for i in range(len(inputs)):
            line_number = str(i + 1)

            file.write(" ".join([line_number, inputs[i], "\n"]))


arguments = sys.argv

path = create_directories(arguments)

file_name = find_file_name(arguments)

if file_name:
    inputs = handle_input()

    append_to_file(path, file_name, inputs)
