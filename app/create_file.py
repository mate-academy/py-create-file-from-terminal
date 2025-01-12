import datetime
import os
import sys


def create_directory(directory: str) -> None:
    os.makedirs(os.path.join(os.getcwd(), directory))


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        current_date = datetime.datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        for line in sys.stdin:
            if line.rstrip() == "stop":
                break
            file.write(str(line_number) + " " + line)
            line_number += 1
        file.write("\n")


def main_function() -> None:
    input_data = sys.argv
    if "-d" in input_data and "-f" not in input_data:
        create_directory(os.path.join(*input_data[2:]))
    if "-f" in input_data and "-d" not in input_data:
        create_file(input_data[-1])
    if "-d" in input_data and "-f" in input_data:
        input_data.remove("-f")
        create_directory(os.path.join(*input_data[2:len(input_data) - 1]))
        create_file(os.path.join(*input_data[2:]))


main_function()
