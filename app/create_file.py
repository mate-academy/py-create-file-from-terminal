from datetime import datetime
import os
import sys


def create_file_with_input_text(path: str) -> None:
    input_text = ""
    line_count = 0

    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        line_count += 1
        input_text += f"{line_count} {content_line}\n"

    with open(path, "a") as file_to_write, open(path, "r") as file_to_read:
        if file_to_read.read():
            file_to_write.write("\n")

        current_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        file_to_write.write(f"{current_time}\n{input_text}")


def create_directories(directories_names: list) -> str:
    path = os.path.join(*directories_names)
    os.makedirs(path, exist_ok=True)
    return str(path)


def create_file_from_terminal(variables: list) -> None:
    if "-d" in variables and "-f" in variables:
        directories_names = (
            variables[variables.index("-d") + 1:variables.index("-f")]
        )
        file_name = variables[-1]

        directories = create_directories(directories_names)
        create_file_with_input_text(os.path.join(directories, file_name))

    elif "-d" in variables:
        directories_names = (
            variables[variables.index("-d") + 1:]
        )
        create_directories(directories_names)

    elif "-f" in variables:
        create_file_with_input_text(variables[-1])


create_file_from_terminal(sys.argv)
