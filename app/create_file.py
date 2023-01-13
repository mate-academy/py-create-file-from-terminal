from datetime import datetime
from create_directory import create_directory
import os


def create_file(file_name: str, path: str) -> None:
    with open(os.path.join(path, file_name), "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S%\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.strip() == "stop":
                break
            new_file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    file_name, path = create_directory()
    if file_name:
        create_file(file_name, path)
