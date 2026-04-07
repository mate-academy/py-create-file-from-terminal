import sys
import os
import datetime


def create_dir(path: list[str]) -> None:
    os.makedirs(os.path.join(*path), exist_ok=True)


def create_file(file_name: str) -> None:
    line_number = 1
    with open(file_name, "a") as content_file:
        content_file.write(datetime.datetime.now().
                           strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                content_file.write("\n")
                break
            content_file.write(str(line_number) + " " + text + "\n")
            line_number += 1


def create_content() -> None:
    command = sys.argv[1:]
    if command[0] == "-d":
        try:
            f_index = command.index("-f")
            create_dir(command[1: f_index])
            os.chdir(os.path.join(*command[1: f_index]))
            for file_name in command[f_index + 1:]:
                create_file(file_name)

        except ValueError:
            create_dir(command[1:])
    elif command[0] == "-f":
        try:
            d_index = command.index("-d")
            create_dir(command[d_index + 1:])
            os.chdir(os.path.join(*command[d_index + 1:]))
            for file_name in command[1: d_index]:
                create_file(file_name)

        except ValueError:
            for file_name in command[1:]:
                create_file(file_name)
    else:
        print("Invalid command syntaxis")


create_content()
