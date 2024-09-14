from datetime import datetime
import sys
import os


def working_with_file(file_name: str) -> None:
    with open(f"{file_name}", "a") as file:

        formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{formatted_date}\n")
        num = 1

        while True:
            line = input("Enter content line:")
            if line == "stop":
                break

            file.write(f"{num} {line}\n")
            num += 1


def working_with_directories(args: list) -> None:
    directories = []

    for i in range(args.index("-d") + 1, len(args), 1):

        element = args[i]
        if element == "-f":
            break

        directories.append(element)

    for directory in directories:

        if os.path.isdir(directory):
            os.chdir(directory)

        else:
            os.mkdir(f"{directory}")
            os.chdir(f"{directory}")


def detect_keys(args: list) -> None:

    if "-d" in args:
        working_with_directories(args)

    if "-f" in args:
        working_with_file(args[args.index("-f") + 1])


detect_keys(sys.argv)
