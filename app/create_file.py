import sys
from os import path, makedirs
from datetime import datetime


class InvalidInputError(Exception):
    pass


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
        raise InvalidInputError("Usage: python create_file.py "
                                "-d <dir_path> or -f <file_path>")

    flag = sys.argv[1]

    if flag == "-d":
        if len(sys.argv) < 3:
            raise InvalidInputError("Please provide a directory "
                                    "path after -d flag.")
        if "-f" in sys.argv:
            if len(sys.argv) < 4:
                raise InvalidInputError("Please provide directory "
                                        "and file paths after -d -f flags.")
            directory_path = path.join(*sys.argv[2:-2])
            makedirs(directory_path)
            create_file(path.join(directory_path, sys.argv[-1]))
        else:
            directory_path = path.join(*sys.argv[2:])
            makedirs(directory_path)

    elif flag == "-f":
        if len(sys.argv) < 3:
            raise InvalidInputError("Please provide a file name "
                                    "after -f flag.")
        file_path = sys.argv[2]
        create_file(file_path)

    else:
        raise InvalidInputError(f"Invalid flag: {flag}")


if __name__ == "__main__":
    main()
