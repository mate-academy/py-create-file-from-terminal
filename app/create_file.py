import sys
import os
from datetime import datetime


def create_file(dir_path: str, file_name: str) -> callable:
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)
    mode = "a" if os.path.isfile(file_path) else "w"
    with open(file_path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
    return file


def write_content(new_file: object) -> None:
    counter = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        new_file.write(f"{counter} {content} \n")
        counter += 1


def main(args: list) -> None:
    dir_path = ""
    file_name = ""
    for index in range(len(args)):
        if args[index] == "-d":
            dir_path = "/".join(args[index + 1:])
        elif args[index] == "-f":
            file_name = args[index + 1]
    if not dir_path or not file_name:
        print("Please provide valid directory path and file name")
        return
    file_new = create_file(dir_path, file_name)
    write_content(file_new)


if __name__ == "__main__":
    main(sys.argv)
