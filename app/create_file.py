import datetime
import os
import sys


def add_information_to_file(file_name: str) -> None:
    with open(file_name, "a") as document:
        data_inf = f"{datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n"
        document.write(data_inf)

        count = 0

        while True:
            text_input = input("Enter content line: ")
            count += 1
            if text_input == "stop":
                break
            else:
                document.write(f"{count} {text_input}\n")
        document.write("\n")


def directory_file_creation() -> None:

    if "-d" in sys.argv:
        count = 2
        while count != len(sys.argv) and sys.argv[count] != "-f":
            os.mkdir(sys.argv[count])
            os.chdir(sys.argv[count])
            count += 1

    if "-f" in sys.argv:
        add_information_to_file(sys.argv[-1])


directory_file_creation()
