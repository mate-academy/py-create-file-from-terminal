from datetime import datetime
import sys
import os


args = sys.argv


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


def working_with_directories() -> None:
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


if "-d" in args:
    working_with_directories()

if "-f" in args:
    working_with_file(args[args.index("-f") + 1])
