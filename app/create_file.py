import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")


def create_file(path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name)
    with open(file_path, "a") as file_result:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_result.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.strip().lower() == "stop":
                break
            file_result.write(f"{line_number} {content}\n")
            line_number += 1
    print(f"File '{file_path}' created/updated successfully.")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            directories = args[d_index + 1:]
            file_name = None

        if directories:
            dir_path = os.path.join(*directories)
            create_directory(dir_path)

        if file_name:
            create_file(dir_path, file_name)
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(".", file_name)
    else:
        print("Usage:")
        print("  python create_file.py -d <directories> -f <file_name>")
        print("  python create_file.py -f <file_name>")


if __name__ == "__main__":
    main()
