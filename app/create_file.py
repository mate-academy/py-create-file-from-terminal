import sys
import os
import datetime


def write_into_file():
    with open(sys.argv[-1], "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        number = 1
        while True:
            message = input("Enter content line: ")
            if message != "stop":
                file.write(f"{number} {message}\n")
                number += 1
            else:
                file.write("\n")
                break


def make_dir():
    for name in sys.argv[2:]:
        if not os.path.exists(name):
            os.makedirs(name)


def make_dir_inside_dir():
    for name in sys.argv[2: len(sys.argv) - 2]:
        if not os.path.exists(name):
            os.mkdir(name)
            os.chdir(name)
        else:
            os.chdir(name)


def create_file():
    if len(sys.argv) < 2:
        return

    elif "-f" in sys.argv and "-d" in sys.argv:
        make_dir_inside_dir()
        write_into_file()

    elif sys.argv[1] == "-d":
        make_dir()

    elif sys.argv[1] == "-f":
        write_into_file()

    else:
        print("Please, use correct query!")


create_file()
