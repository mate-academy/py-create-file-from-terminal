import datetime
import os
import sys


arguments = sys.argv

if arguments:

    path = []
    file_name = ""

    for argument in arguments[1:]:
        if argument == "-f":
            file_name = arguments[-1]
            break

        if argument == "-d":
            continue
        path.append(argument)

    if path:
        str_path = os.path.join(*path)
        if not os.path.exists(str_path):
            os.makedirs(str_path)

    def write_in_file(file_path: str, line: str, number: str) -> None:
        with open(file_path, "a") as file:
            file.write(f"{number}{line}\n")

    if file_name:
        path_to_file = os.path.join(*path, file_name)

        timestamp = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        write_in_file(path_to_file, timestamp, "")

        lines_number = 1
        while True:
            content = input("Enter content line: ")

            if content == "stop":
                break
            write_in_file(path_to_file, content, f"{lines_number} ")
            lines_number += 1

        write_in_file(path_to_file, "", "")
