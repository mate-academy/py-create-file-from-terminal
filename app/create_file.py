import os
import sys
from datetime import datetime


def create_file(data: list[str]) -> str:
    file_name = ""
    folders_name = ""

    if "-d" in data and "-f" not in data:
        folders_name = os.path.join(*data[2:])

    elif "-f" in data and "-d" not in data:
        file_name = os.path.join(*data[2:])

    elif "-d" in data and "-f" in data:
        start_directory_index = (data.index("-d") + 1)
        file_index = (data.index("-f") + 1)
        if file_index > start_directory_index:
            folders_name = (
                os.path.join(*data[start_directory_index:data.index("-f")])
            )
        else:
            folders_name = os.path.join(*data[start_directory_index:])
        file_name = data[file_index]

    os.makedirs(folders_name, exist_ok=True)
    return os.path.join(folders_name, file_name)


def writing_to_file() -> None:
    data = sys.argv
    with open(create_file(data), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    writing_to_file()
