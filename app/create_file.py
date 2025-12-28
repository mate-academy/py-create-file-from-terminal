from sys import argv
from os import makedirs, path
from datetime import datetime


terminal = argv[1:]


def write_into_file(our_path: str) -> None:
    our_path = path.join(our_path, terminal[-1])
    with open(our_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            file_text = input("Enter content line: ")
            if file_text == "stop":
                break
            file.write(file_text + "\n")


def d_and_f_flags() -> None:
    our_path = path.join(*terminal[1:terminal.index("-f")])
    makedirs(our_path)
    write_into_file(our_path)


def d_flag() -> None:
    our_path = path.join(*terminal[1:])
    makedirs(our_path)


def f_flag() -> None:
    our_path = path.join(*terminal[1:])
    write_into_file(our_path)


if "-f" in terminal and "-d" in terminal:
    d_and_f_flags()
elif "-d" in terminal:
    d_flag()
else:
    f_flag()
