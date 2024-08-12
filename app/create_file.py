import sys
from datetime import datetime
from pathlib import Path


def create_file() -> None:
    file_name = ""
    arguments = sys.argv[1:]

    # If command like have both -d and -f keyword
    if "-d" in arguments and "-f" in arguments:
        for key, value in enumerate(arguments):
            if value == "-d":
                start = key
            elif value == "-f":
                end = key

        # Searching path. For example we have command:
        # python create_file.py -d dir1 dir2 dir3 -f text.txt
        # we will search index of -d, after index of -f and next
        # we will take only this part: ['dir1', 'dir2', 'dir3']
        path_dir = Path(*arguments[start + 1:end])
        path_dir.mkdir(parents=True, exist_ok=True)
        file_name = path_dir / arguments[len(arguments) - 1]
        print(file_name)

    # If command like have only -f keyword
    elif arguments[0] == "-f":
        file_name = arguments[1]

    # If command like have only -d keyword
    elif arguments[0] == "-d":
        path_dir = Path(*arguments[1:])
        path_dir.mkdir(parents=True, exist_ok=True)
        file_name = path_dir / "file.txt"

    # Open write to the file
    with open(file_name, "a") as file:
        file.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        counter = 0
        while True:
            counter += 1
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"{counter} {new_line}\n")
