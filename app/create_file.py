import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory {path} created successfully.")


def create_file(file_path: str) -> None:
    directory = os.path.dirname(file_path)
    if directory:
        create_directory(directory)

    file_exists = os.path.exists(file_path)
    mode = "a" if file_exists else "w"

    with open(file_path, mode) as f:
        if file_exists:
            f.write("\n")
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        if d_index < f_index:
            path = os.path.join(*args[d_index + 1:f_index])
            file_name = args[f_index + 1]
        else:
            path = os.path.join(*args[d_index + 1:])
            file_name = args[f_index + 1]

        file_path = os.path.join(path, file_name)
        create_file(file_path)

    elif "-d" in args:
        path = os.path.join(*args[args.index("-d") + 1:])
        create_directory(path)

    elif "-f" in args:
        file_name = args[args.index("-f") + 1]
        create_file(file_name)

    else:
        print("Invalid arguments. "
              "Please use -d for directory and/or -f for file.")


if __name__ == "__main__":
    main()
