import datetime
import os
import sys


def create_directory(path_parts: list[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    append_mode = "a" if os.path.exists(file_name) else "w"
    with open(file_name, append_mode) as file:
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    directory = []
    file_name = None
    args = sys.argv[1:]

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directory.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
            i += 1
        else:
            i += 1

    if directory:
        path = create_directory(directory)
    else:
        path = os.getcwd()

    if file_name:
        file_path = os.path.join(path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
