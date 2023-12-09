import sys
import os

import datetime


def create_directory(directorys: list) -> None:
    for _ in range(len(directorys)):
        try:
            os.mkdir(os.path.join(directorys[:_]))
        except FileExistsError:
            continue


def create_file_in_directory(path_to_file: list) -> None:
    with open(os.path.join(*path_to_file), "a") as f:
        f.close()


def writing_into_file(path: list, content: list) -> None:

    with open(os.path.join(*path), "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n"
        )

        string_number = 0
        for line in content:
            if line == "\n":
                file.write(line)
                break

            string_number += 1
            file.write(str(string_number) + " ")
            file.write(line + "\n")


if __name__ == "__main__":

    file_directory = []
    content_to_file = []

    for i in range(len(sys.argv)):

        if sys.argv[i] == "-d":
            for element in sys.argv[i + 1:]:
                if element == "-f":
                    break

                file_directory.append(element)
            create_directory(file_directory)

        if sys.argv[i] == "-f":

            full_file_path = file_directory + [sys.argv[i + 1]]
            create_file_in_directory(full_file_path)

            while True:
                content_line = input("Enter content line:")

                if content_line == "stop":
                    content_to_file.append("\n")
                    break

                content_to_file.append(content_line)

            writing_into_file(full_file_path, content_to_file)
