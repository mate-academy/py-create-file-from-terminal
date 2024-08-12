from datetime import datetime
import os
import sys
from sys import argv as arguments


def create_file(file_name: str) -> None:
    if os.path.exists(file_name):
        key = "a"
    else:
        key = "w"
    with open(file_name, key) as writer:
        if key == "a":
            writer.write("\n")
        writer.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        counter = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            writer.write(str(counter) + " " + line + "\n")
            counter += 1


def create_path(names: str) -> None:
    try:
        os.makedirs(names, exist_ok=False)
    except Exception:
        pass
    if "-f" in sys.argv:
        os.chdir(names)


def create_file_from_console() -> None:
    for i in range(len(arguments)):

        if arguments[i] == "-f":
            try:
                create_file(arguments[i + 1])
            except ValueError as e:
                print(f"Error: {e}\n Write correct file name!")

        if arguments[i] == "-d":
            path_names = []
            while arguments[i + 1] != "-f":
                try:
                    path_names.append(arguments[i + 1])
                    i += 1
                except IndexError:
                    break
            create_path("/".join(path_names))


create_file_from_console()
