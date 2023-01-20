import os
import sys
from datetime import datetime


def main(arguments):
    value_is_f = False
    value_is_d = False
    path = os.getcwd() + "\\"

    for value in arguments:
        if value == "-f":
            value_is_d = False
            value_is_f = True

        if value == "-d":
            value_is_d = True
            value_is_f = False

        if value_is_f and value != "-f":
            create_file(value, path)

        if value_is_d and value != "-d":
            if value != "-f":
                path += value + "\\"
                try:
                    os.mkdir(path)
                except OSError:
                    pass


def create_file(name_of_file, path):
    now = datetime.now()
    name_of_file = path + name_of_file

    with open(name_of_file, "a") as new_file:
        new_file.write(now.strftime("%Y-%m-%d %H:%M:%S\n"))
        counter = 1

        while True:
            line = input("Enter content line: ")

            if line.lower() == "stop":
                break

            new_file.write(str(counter) + " " + line + "\n")
            counter += 1
        new_file.write("\n")


if __name__ == "__main__":
    main(sys.argv)
