import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    try:
        os.makedirs(path)
        print(f"Created directory: {path}")
    except FileExistsError:
        print(f"Directory already exists: {path}")
    except OSError as e:
        print(f"Failed to create directory: {path}")
        print(f"Error: {str(e)}")


def create_file(file_path: str) -> None:
    try:
        with open(file_path, "a") as file:
            file.write("\n")
            print(f"Created file: {file_path}")
    except OSError as e:
        print(f"Failed to create file: {file_path}")
        print(f"Error: {str(e)}")


def get_timestamp() -> str:
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def append_content(file_path: str, lines: list) -> None:
    try:
        with open(file_path, "a") as file:
            file.write("\n")
            file.write(get_timestamp())
            file.write("\n")
            for line in lines:
                file.write(line)
                file.write("\n")
            print(f"Added content to file: {file_path}")
    except OSError as e:
        print(f"Failed to add content to file: {file_path}")
        print(f"Error: {str(e)}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Please provide arguments.")
        return

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        if d_index < f_index:
            directory_path = os.path.join(*args[d_index + 1:f_index])
            create_directory(directory_path)
            file_name = args[f_index + 1]
            file_path = os.path.join(directory_path, file_name)
            create_file(file_path)
            lines = []
            while True:
                line = input("Enter content line: ")
                if line.lower() == "stop":
                    break
                lines.append(line)
            append_content(file_path, lines)
        else:
            print("Invalid arguments.")
    else:
        print("Invalid arguments.")


if __name__ == "__main__":
    main()

