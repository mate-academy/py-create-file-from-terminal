import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def python_create_file(directory: str, name: str) -> None:
    path_to_file = os.path.join(directory, name)

    with open(path_to_file, "w") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        print("Enter content line")

        line_number = 1
        while True:
            line = input()
            if line.lower() == "stop":
                break

            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    index_d = 0
    index_f = 0

    for i, arg in enumerate(sys.argv):
        if arg == "-d":
            index_d = i + 1
        elif arg == "-f":
            index_f = i + 1

    if index_d is not None and index_f is not None:
        path = os.path.join(*sys.argv[index_d:index_f - 1])
        python_create_file(path, sys.argv[index_f])
        create_directory(path)

    elif index_d is not None:
        path = os.path.join(*sys.argv[index_d:])
        create_directory(path)

    elif index_f is not None:
        path = os.path.join(*sys.argv[:index_f - 1])
        create_directory(path)
        python_create_file(path, sys.argv[index_f])


if __name__ == "__main__":
    main()
