import os
import sys
from datetime import datetime
from typing import Optional


def create_file(directory: Optional[str], filename: str) -> None:
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    file_path = filename
    if directory:
        file_path = os.path.join(directory, filename)

    with open(file_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    directory = None
    filename = None
    args = iter(sys.argv[1:])
    for arg in args:
        if arg == "-d":
            directory = next(args)
        elif arg == "-f":
            filename = next(args)

    if not filename:
        print("Error: No filename provided.")
        return

    create_file(directory, filename)


if __name__ == "__main__":
    main()
