import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    return os.path.join(*directories)


def create_file(args: list = None) -> None:
    if args is None:
        args = sys.argv[1:]
    if not args:
        return

    directory = []
    file_name = ""

    for index, element in enumerate(args):
        if (element == "-f"
                and index + 1 < len(args)
                and not args[index + 1].startswith("-")):
            file_name = args[index + 1]

        if element == "-d":
            next_index = index + 1
            while (next_index < len(args)
                   and not args[next_index].startswith("-")):
                directory.append(args[next_index])
                next_index += 1

    if directory:
        os.makedirs(create_path(directory), exist_ok=True)

    if file_name == "":
        return

    full_path = create_path(directory + [file_name])

    file_exists_with_content = (
        os.path.exists(full_path) and os.path.getsize(full_path) > 0
    )

    first_line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a") as source_file:
        if file_exists_with_content:
            source_file.write("\n")
        source_file.write(first_line + "\n")

        counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            source_file.write(f"{counter} {line}\n")
            counter += 1


create_file()
