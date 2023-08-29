import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except FileNotFoundError:
            print("Unsupported characters in file path!!!")
            sys.exit()
    return path


def create_file(path: str) -> None:
    with open(path, "w") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_count = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            line_count += 1
            file.write(f"{line_count}. {content}\n")


if __name__ == "__main__":
    terminal_input = sys.argv
    if "-f" not in terminal_input and "-d" not in terminal_input:
        print(
            " Please, provide a valid command:"
            "'-d <directory_1> <directory_2>' or '-f <file_name>'"
        )
        sys.exit()
    if "-d" not in terminal_input:
        if len(terminal_input) < 3:
            print("'file_name' argument is missing")
            sys.exit()
        try:
            _, flag_f, file_name, *_ = terminal_input
            if flag_f != "-f":
                print("Provide command in a valid format: '-f <file_name>'")
                sys.exit()
            create_file(file_name)
        except ValueError:
            print("'file_name' argument is missing")
            print("Provide a file name in a valid format: '-f <file_name>'")
    if "-f" not in terminal_input:
        if len(terminal_input) < 3:
            print("'directory' argument is missing")
            sys.exit()
        try:
            _, flag_d, *directories = terminal_input
            if flag_d != "-d":
                print(
                    "Provide command in a valid format: "
                    "'-d <directory_1> <directory_2>...'"
                )
                sys.exit()
            path = create_path(directories)
        except TypeError:
            print(
                "'directory' argument is missing\n"
                "Provide directory(ies) in a valid format: "
                "'-d <directory_1> <directory_1>...'"
            )
    if "-f" in terminal_input and "-d" in terminal_input:
        if terminal_input[-1] == "-f":
            if terminal_input[1] == "-f":
                print("'directory' argument is missing")
            print("'file_name' argument is missing")
            sys.exit()
        if terminal_input.index("-d") > terminal_input.index("-f"):
            print(
                " Please, provide commands in a valid order:"
                "'-d <directory_1> <directory_2>... -f <file_name>'"
            )
            sys.exit()
        _, flag_d, *directories, flag_f, file_name = terminal_input
        if not directories:
            print("'directory' argument is missing")
            sys.exit()
        path = fr"{create_path(directories)}\{file_name}"
        create_file(path)
