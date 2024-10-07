import os
import sys
from datetime import datetime


def create_file(path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name)
    if not os.path.exists(path):
        os.makedirs(path)

    if os.path.exists(file_path):
        print(f"File {file_name} already exists. Appending content...")
    else:
        print(f"Creating file {file_name}...")

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        path_parts = []
        for arg in args[d_index + 1]:
            if arg.startswith("-f"):
                break
            path_parts.append(arg)
        path = os.path.join(*path_parts)
    else:
        path = os.getcwd()
    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(path, file_name)
    else:
        print("Error: No file specified. Use -f to specify file name.")


if __name__ == "__main__":
    main()
