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

    if file_name:
        path_to_file = os.path.join(*path, file_name)

        timestamp = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        content = f"\n\n{timestamp}"

        if not os.path.exists(path_to_file):
            content = timestamp

        line_number = 1
        while True:
            user_input = input("Enter content line: ")

            if user_input == "stop":
                break

            content += f"\n{line_number} {user_input}"
            line_number += 1

        with open(path_to_file, "a") as file:
            file.write(content)
