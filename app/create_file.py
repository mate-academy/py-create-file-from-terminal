import os
import sys
from datetime import datetime


def create_file() -> str:
    date = sys.argv
    file_name = ""
    folders_name = ""

    if "-d" in date and "-f" not in date:
        folders_name = os.path.join(date[3], date[4])

    elif "-f" in date and "-d" not in date:
        file_name = os.path.join(date[2])

    elif "-d" in date and "-f" in date:
        d_index = (date.index("-d") + 1)
        folders_name = "/".join(date[d_index:date.index("-f")])
        f_index = (date.index("-f") + 1)
        file_name = date[f_index]

    os.makedirs(folders_name, exist_ok=True)
    return f"{folders_name}/{file_name}"


def file_completion() -> None:
    with open(create_file(), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    file_completion()
