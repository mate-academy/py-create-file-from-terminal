from datetime import datetime
import os
from sys import argv


def create_file(path_with_file: str) -> None:
    with open(os.path.join(path_with_file), "w") as file:
        content = ""
        while True:
            line = str(input("Enter content line: "))
            if line == "stop":
                break
            content += line + "\n"
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write(content)


def create_path(path_to_create: list) -> str:
    # creating path from list
    return os.path.join("/".join(path_to_create))


if "-f" in argv and "-d" in argv:
    path = []
    for arg in argv[2:]:
        if arg == "-f":
            break
        path.append(arg)
    os.makedirs(create_path(path))  # making directories
    path.append(argv[-1])  # making path with file
    create_file(create_path(path))  # creating file with path with file

elif argv[1] == "-d":
    path = create_path(argv[2:])
    os.makedirs(path)  # create just a path if -d is an only flag

elif argv[1] == "-f":
    create_file(argv[2])  # create just a file if -f is an only flag
