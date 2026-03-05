import sys
import os
from datetime import datetime


def get_command() -> list:
    return sys.argv[1:]


def get_file_content(file_path: str) -> None:
    with open(file_path, "a") as file:
        time = datetime.now()
        file.write(time.strftime("%Y-%m-%d %H:%M:%S\n"))
        line_counter = 0
        while True:
            line_counter += 1
            content_line = input("Enter content line: ")
            if content_line == "stop":
                break
            line_content = f"{line_counter} {content_line}\n"
            file.write(line_content)
        file.write("\n")


def create_file() -> None:
    command = get_command()
    if "-f" not in command:
        os.makedirs(os.path.join(*(["app"] + command[1:])))
    elif "-d" not in command:
        get_file_content(os.path.join("app", command[1]))
    else:
        if command[0] == "-d":
            os.makedirs(os.path.join(*(["app"] + command[1:-2])))
            file_path = os.path.join(os.path.join(*(["app"] + command[1:-2])),
                                     command[-1])
        else:
            os.makedirs(os.path.join(*(["app"] + command[3:])))
            file_path = os.path.join(*(["app"] + command[3:]), command[1])
        get_file_content(file_path)


if __name__ == "__main__":
    create_file()
