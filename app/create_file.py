import sys
import os

import datetime


def create_file(path: list) -> None:

    for path_element in path[:-1]:
        try:
            os.mkdir(os.path.join(path_element))
        except FileExistsError:
            continue

    with open("/".join(path), "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":

    created_file_path = []

    for i in range(len(sys.argv)):

        if sys.argv[i] == "-d":
            for element in sys.argv[i + 1:]:
                if element == "-f":
                    break

                created_file_path.append(element)

        if sys.argv[i] == "-f":
            created_file_path.append(sys.argv[i + 1])

    create_file(created_file_path)
