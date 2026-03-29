import datetime
import os
import sys


def get_path_and_file_name() -> tuple:
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
            path = os.path.join(*path)
            if not os.path.exists(path):
                os.makedirs(path)

            return path, file_name
        return "", file_name


def process_user_input() -> tuple:
    path, file_name = get_path_and_file_name()
    content = ""
    path_to_file = ""

    if file_name:
        path_to_file = os.path.join(path, file_name)

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

    return content, path_to_file


def write_in_file() -> None:
    content, path_to_file = process_user_input()
    if path_to_file:
        with open(path_to_file, "a") as file:
            file.write(content)


if __name__ == "__main__":
    write_in_file()
