import os
import sys
from datetime import datetime


def create_directory() -> None:
    first_dir, second_dir = sys.argv[2:4]
    path = os.path.join(first_dir, second_dir)
    os.makedirs(path)


def create_file(file_path: str = sys.argv[2]) -> None:
    current_date_time = datetime.now()
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(current_date_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            line_number = 1
            while True:
                file_content = input("Enter content line: ")
                if file_content.lower().strip() == "stop":
                    break
                file.write(f"{line_number} {file_content}\n")
                line_number += 1
    else:
        with open(file_path, "a") as file:
            file.write("\n")
            file.write(current_date_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            line_number = 1
            while True:
                file_content = input("Enter content line: ")
                if file_content.lower().strip() == "stop":
                    break
                file.write(f"{line_number} {file_content}\n")
                line_number += 1


def create_both() -> None:
    create_directory()
    folder_1, folder_2 = sys.argv[2:4]
    file_name = sys.argv[5]
    path = os.path.join(folder_1, folder_2, file_name)
    create_file(file_path=path)


def main() -> None:
    if len(sys.argv) == 4 and sys.argv[1] == "-d":
        create_directory()

    if len(sys.argv) == 3 and sys.argv[1] == "-f":
        create_file()

    if len(sys.argv) == 6:
        if sys.argv[1] == "-d" and sys.argv[4] == "-f":
            create_both()
