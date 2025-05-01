import datetime
import os
from sys import argv
from typing import Union

from typing_extensions import LiteralString


def create_directory(path_parts: list) -> Union[LiteralString, str, bytes]:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")
    return path


def create_file(file_name: Union[LiteralString, str, bytes]) -> None:
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)
    current_date = datetime.datetime.now()
    date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.isfile(file_name) else "w"
    with open(file_name, mode) as f:
        f.write(f"\n{date_time}\n")
        f.write("\n".join(content))

    print(f"File was created: {file_name}")


def main() -> None:
    args = argv[1:]
    print(args)
    directory_path = os.getcwd()
    print(directory_path)
    file_name = None
    i = 0
    while i < len(args):
        # If only -f flag passed, means first item is the file name.
        if args[i] == "-f":
            i += 1
            file_name = args[i]
            i += 1
        # If only -d flag passed, means all items
        # after this flag are parts of the path.
        elif args[i] == "-d":
            i += 1
            dir_parts = []
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            if dir_parts:
                directory_path = create_directory(dir_parts)
    if file_name:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
