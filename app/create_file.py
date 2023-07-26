import os
import sys
from datetime import datetime


def create_directory(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def write_to_file(file_name: str) -> None:
    if not os.path.isfile(file_name):
        with open(file_name, "w") as new_file:
            date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_file.write(date_today + "\n")
            number = 0
            while True:
                content = input("Enter content line: ")
                if content != "stop":
                    new_file.write(f"{1 + number} {content}\n")
                    number += 1
                else:
                    break
    else:
        with open(file_name, "a") as existing_file:
            date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            existing_file.write("\n" + date_today + "\n")
            number = 0
            while True:
                content = input("Enter content line: ")
                if content != "stop":
                    existing_file.write(f"{1 + number} {content}\n")
                    number += 1
                else:
                    break


def main() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        directory_path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        create_directory(directory_path)

    if "-f" in sys.argv and "-d" not in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        write_to_file(file_name)

    if "-d" in sys.argv and "-f" in sys.argv:
        directory_path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        file_name = sys.argv[sys.argv.index("-f") + 1]
        create_directory(directory_path)
        os.chdir(directory_path)
        write_to_file(file_name)


if __name__ == "__create_file__":
    main()
