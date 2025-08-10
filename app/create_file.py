import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Директорію створено: {path}")


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        print(f"Файл створено: {file_path}")
        line_number = 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                f.write("\n")
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    console_arg = sys.argv[1:]
    directory_parts = []
    file_name = None
    creating_directory = False

    for arg in console_arg:
        if "-d" == arg:
            creating_directory = True
        elif "-f" == arg:
            creating_directory = False
        else:
            if creating_directory:
                directory_parts.append(arg)
            elif file_name is None:
                file_name = arg

    if directory_parts:
        directory_path = os.path.join(os.getcwd(), *directory_parts)
        create_directory(directory_path)

    if file_name:
        if directory_parts:
            file_name = os.path.join(directory_path, file_name)

        file_name = os.path.join(os.getcwd(), file_name)
        create_file(file_name)


if __name__ == "__main__":
    main()
