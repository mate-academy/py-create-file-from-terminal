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


def create_file(file_name: str, path: list = None) -> None:
    if path:
        os.makedirs("/".join(path))
        file_name = f"{'/'.join(path)}/{file_name}"
    add_information_to_file(file_name)


def directory_file_creation() -> None:
    entered_info = sys.argv

    if "-d" in entered_info and "-f" not in entered_info:
        folders_name = ''
        for i in range(2, len(entered_info)):
            folders_name += f"{entered_info[i]}\\"
        path = os.path.join(folders_name)
        os.makedirs(path)

    if "-f" in entered_info and "-d" not in entered_info:
        create_file(entered_info[-1])

    if "-f" in entered_info and "-d" in entered_info:
        file_name = entered_info[-1]
        path = entered_info[
            (entered_info.index("-d") + 1):entered_info.index("-f")
        ]
        create_file(file_name, path)

