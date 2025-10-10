import os
import sys
from datetime import datetime


def create_directory(directory_path: str) -> str:
    os.makedirs(directory_path)
    return directory_path


def create_file(file_path: str) -> None:
    file_data = []
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        file_line = input("Enter content line: ")

        if file_line.strip().lower() == "stop":
            break

        file_data.append(file_line)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(current_timestamp + "\n")

        for i, file_line in enumerate(file_data, 1):
            file.write(f"{i} {file_line}")

        file.write("\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Enter this command: python create_file.py -d directory_path -f file_path")
        return

    directory_path = ""

    if "-d" in args:
        d_index = args.index("-d") + 1

        if "-f" in args:
            f_index = args.index("-f")
            directory_parts = args[d_index:f_index]
        else:
            directory_parts = args[d_index:]

        directory_path = create_directory(os.path.join(*directory_parts))

    file_name = ""

    if "-f" in args:
        f_index = args.index("-f") + 1
        file_name = args[f_index]

        full_file_path = (
            os.path.join(directory_path, file_name)
            if directory_path else file_name
        )

        create_file(full_file_path)


if __name__ == "__main__":
    main()
