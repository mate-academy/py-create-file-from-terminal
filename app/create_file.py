import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    path = ""

    file_index = None

    if "-f" in args:
        file_index = args.index("-f")

    if "-d" in args:
        directory_index = args.index("-d")

        if file_index is not None and file_index > directory_index:
            directory = args[directory_index + 1:file_index]
        else:
            directory = args[directory_index + 1:]

        if directory:
            path = os.path.join(*directory)
            os.makedirs(path, exist_ok=True)

    if "-f" not in args:
        return

    file_name = args[file_index + 1]
    file_path = os.path.join(path, file_name)

    with open(file_path, "a", encoding="utf-8") as source_file:
        if os.path.getsize(file_path) > 0:
            source_file.write("\n")

        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(current_date + "\n")

        number = 1

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break

            source_file.write(f"{number} {line}\n")
            number += 1


create_file()
