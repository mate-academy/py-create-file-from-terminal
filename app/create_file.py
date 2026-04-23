import os
import datetime
import argparse


def create_file_from_terminal() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", nargs="+", dest="parts_of_path")
    parser.add_argument("-f", nargs="+", dest="file_name")
    args = parser.parse_args()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    final_directory = os.getcwd()
    if args.parts_of_path is not None:
        final_directory = os.path.join(final_directory, *args.parts_of_path)
        os.makedirs(final_directory)
    if args.file_name is not None:
        final_directory = os.path.join(final_directory, *args.file_name)

        with open(final_directory, "a") as f:
            f.write(f"{current_time}\n")
            line_number = 1
            while True:
                input_from_user = input("Enter content line: ")
                if input_from_user == "stop":
                    break
                f.write(f"{line_number} {input_from_user}\n")
                line_number += 1
