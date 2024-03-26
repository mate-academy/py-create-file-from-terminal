import os
import sys
import datetime


def create_file_and_dir():
    pass


def create_data_for_file():
    if "-d" in sys.argv:
        os.makedirs("/".join(sys.argv[2:]))
    if "-f" in sys.argv:
        with open(sys.argv[-1], "a") as f:
            f.write(str(datetime.datetime.now()) + "\n")
            file_contents = input("Enter content line: ")
            number_of_lines = 1
            while file_contents != "stop":
                f.write(f"{number_of_lines} {file_contents}\n")
                file_contents = input("Enter content line: ")
                number_of_lines += 1
            f.write("\n")


if __name__ == "__main__":
    create_data_for_file()
