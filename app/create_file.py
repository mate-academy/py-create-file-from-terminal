from datetime import datetime
import os
import argparse


def create_file_from_terminal():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", default="file.txt")
    parser.add_argument("-d", nargs="*")
    args = parser.parse_args()

    file_name = args.f
    # will check for directories later
    file_path = file_name

    # create directory path if it was in args
    if args.d:
        directory = "/".join(args.d)

        file_path = f"{directory}/{file_name}"

        if not os.path.exists(directory):
            os.makedirs(directory)

    with open(file_path, "a") as file:
        # creating time stamp when file was created or opened
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # this string would be written to the file. adding time stamp here
        lines_for_write = f"{time_stamp}\n"

        # index that should be at the beginning of each line with text
        index = 1

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines_for_write += f"{index} {line}\n"
            index += 1

        file.write(lines_for_write)


create_file_from_terminal()
