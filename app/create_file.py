import sys
import os
from datetime import datetime
from pathlib import Path


def file_creator(path: str) -> None:
    with open(path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            line = input("Enter line: ")
            if line.strip().lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:

    args = sys.argv[1:]
    if not args:
        print("Arguments are missing!")
        return

    catalogs = []
    created_file = ""
    flag = ""

    for arg in args:
        if arg in ("-d", "-f"):
            flag = arg
        elif flag == "-d":
            catalogs.append(arg)
        elif flag == "-f":
            created_file = arg
            flag = ""

    if not created_file:
        print("Error: Missing file name after '-f' flag.")
        return

    cursor = Path(*catalogs) if catalogs else Path(".")
    if cursor:
        os.makedirs(cursor, exist_ok=True)

    file_path = os.path.join(cursor, created_file) if cursor else created_file

    file_creator(file_path)
    print(f"File '{file_path}' created successfully!")


if __name__ == "__main__":
    main()
