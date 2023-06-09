from sys import argv, exit
import os
from datetime import datetime


def validate_creating_file() -> None:
    path = list()
    file_name = ""

    if "-d" in argv:
        for directory in argv[argv.index("-d") + 1:]:
            if directory == "-f":
                break
            path.append(directory)

        if not path:
            print("Path shouldn't be blank")
            exit()

    if "-f" in argv:
        files_count = 0
        for directory in argv[argv.index("-f") + 1:]:
            if directory == "-d":
                break
            files_count += 1

        if files_count == 0:
            print("Should input files name")
            exit()
        elif files_count > 1:
            print("Should input one file name")
            exit()

        file_name = argv[argv.index("-f") + 1]

    create_file(file_name, path)


def create_file(file_name: str, path: list) -> None:
    if "-d" in argv:
        path = os.path.join(*path)
        os.makedirs(path, exist_ok=True)

    if "-d" in argv and "-f" in argv:
        os.chdir(path)

    if "-f" in argv:
        with open(file_name, "a") as target:
            target.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            line_number = 1

            while True:
                content = input("Enter content line: ")

                if content == "stop":
                    target.write("\n")
                    break

                target.write(f"{line_number} {content}\n")
                line_number += 1


if __name__ == "__main__":
    validate_creating_file()
