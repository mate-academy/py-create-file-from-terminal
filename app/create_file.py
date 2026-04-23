import sys
import os
from datetime import datetime


def create_directory(path_parts: str) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    if not os.path.exists(file_path):
        open(file_path, "w").close()

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1
    print(f"File {file_path} updated successfully.")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else None

        if f_index:
            directories = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
            create_directory(directories)
            file_path = os.path.join(*directories, file_name)
            create_file(file_path)
        else:
            directories = args[d_index + 1:]
            create_directory(directories)
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)
    else:
        print("Invalid arguments.")


if __name__ == "__main__":
    main()
