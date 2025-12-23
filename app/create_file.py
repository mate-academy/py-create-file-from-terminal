import os
import sys
import datetime
from typing import Any


def parse_args(args: str) -> tuple[list[Any], str | None]:
    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return dir_parts, file_name


def write_file(base_path: str, file_name: str) -> None:
    file_path = os.path.join(base_path, file_name)

    with open(file_path, "a", encoding="utf-8") as output_file:
        if os.path.getsize(file_path) > 0:
            output_file.write("\n")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(timestamp + "\n")

        counter = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            output_file.write(f"{counter} {line}\n")
            counter += 1


def main() -> None:
    args = sys.argv[1:]
    dir_parts, file_name = parse_args(args)

    base_path = os.getcwd()

    if dir_parts:
        base_path = os.path.join(base_path, *dir_parts)
        os.makedirs(base_path, exist_ok=True)

    if file_name:
        write_file(base_path, file_name)


if __name__ == "__main__":
    main()
