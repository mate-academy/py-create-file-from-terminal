import datetime
import os
import sys


def accept_content() -> dict:
    string_number = 0
    file_content = {}
    while True:
        string_to_file = input("Enter content line:")
        if string_to_file.lower() == "stop":
            break
        string_number += 1
        file_content.update({string_number: string_to_file})
    return file_content


def write_to_file(path_to_file: str, content_to_file: dict) -> None:
    with open(path_to_file, "+a") as file:
        if os.stat(path_to_file).st_size != 0:
            file.write("\n\n")
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for element in content_to_file:
            file.write("\n")
            file.write(f"{element} {content_to_file.get(element)}")


command_length = len(sys.argv)
file_path = os.getcwd()
if sys.argv[1] == "-d":
    for i in range(2, command_length):
        if sys.argv[i] == "-f":
            file_path = os.path.join(file_path, sys.argv[i + 1])
            write_to_file(file_path, accept_content())
            break
        file_path = os.path.join(file_path, sys.argv[i])
        if not os.path.exists(file_path):
            os.mkdir(file_path)
elif sys.argv[1] == "-f":
    file_path = os.path.join(file_path, sys.argv[2])
    write_to_file(file_path, accept_content())
