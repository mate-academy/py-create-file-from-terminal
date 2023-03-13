import os
import sys
from datetime import datetime


def create_directory(dir_path: str) -> None:
    try:
        os.makedirs(dir_path, exist_ok=True)
        print("Directory created")
    except Exception as e:
        print(f"Error creating directory: {str(e)}")
        sys.exit(1)


def file_content(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{count} {line}\n")
            count += 1


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print("File already exists, you can add something")
        file_content(file_path)

    else:
        try:
            file_content(file_path)
        except Exception as e:
            print(f"Error creating file: {str(e)}")
            sys.exit(1)


def main() -> None:
    args = sys.argv[1:]
    dir_path = ""
    file_path = ""

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        path_parts = args[dir_index + 1:file_index]
        dir_path = os.path.join(*path_parts)
        file_name = args[file_index + 1]
        file_path = os.path.join(*path_parts, file_name)
        create_directory(dir_path)
        create_file(file_path)

    elif "-d" in args:
        dir_index = args.index("-d") + 1
        dir_path = os.path.join(*args[dir_index:])
        create_directory(dir_path)

    elif "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)

    elif not args:
        print(
            "Invalid arguments. Usage: python create_file.py "
            "[-d directory_path] [-f file_name]"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
