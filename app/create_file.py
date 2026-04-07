import sys
import os
import datetime


def create_dir(path: list[str]) -> None:
    os.makedirs(os.path.join(*path), exist_ok=True)


def create_file(file_list: list[str], *path: tuple[str]) -> None:
    for file_name in file_list:
        line_number = 1
        with open(os.path.join(*path, file_name), "a+") as content_file:
            content_file.seek(0)
            if content_file.read():
                content_file.write("\n")
            content_file.write(datetime.datetime.now().
                               strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                content_file.write(str(line_number) + " " + text + "\n")
                line_number += 1


def create_content() -> None:
    command = sys.argv[1:]
    if "-d" in command:
        d_index = command.index("-d")
        if "-f" in command:
            f_index = command.index("-f")
            if f_index > d_index:
                create_dir(command[d_index + 1: f_index])
                create_file(command[f_index + 1:],
                            *command[d_index + 1: f_index])
            else:
                create_dir(command[d_index + 1:])
                create_file(command[f_index + 1: d_index],
                            *command[d_index + 1:])
        else:
            create_dir(command[d_index + 1:])
    elif "-f" in command:
        f_index = command.index("-f")
        create_file(command[f_index + 1:])
    else:
        print("Invalid command syntaxis")


create_content()
