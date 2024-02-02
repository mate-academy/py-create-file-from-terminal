import sys

from os import path, makedirs

from datetime import datetime


class WrongInputError(Exception):
    pass


def create_dir(dir_path: list) -> None:
    directory_path = path.join(*dir_path)
    makedirs(directory_path)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content_line = input(f"Enter content line {line_number} "
                                 f"(or type 'stop' to finish): ")
            if content_line.lower() == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1


def main() -> None:
    if len(sys.argv) < 2:
        raise WrongInputError

    flag = sys.argv[1]
    if flag == "-d":
        if len(sys.argv) < 3:
            raise WrongInputError

        if "-f" in sys.argv:
            create_dir(sys.argv[2: -2])
            create_file(path.join(path.join(*sys.argv[2:-2]), sys.argv[-1]))
        else:
            create_dir(sys.argv[2:])

    elif flag == "-f":
        if len(sys.argv) < 3:
            raise WrongInputError

        create_file(sys.argv[2])


if __name__ == "__main__":
    main()
