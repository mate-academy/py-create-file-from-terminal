import os
import sys
from datetime import datetime


def create_directory(path: any) -> None:
    try:
        os.makedirs(path)
        print(f"Created directory: {path}")
    except OSError as e:
        print(f"Error creating directory: {e}")


def create_file(filename: any) -> None:
    try:
        with open(filename, "a") as file:
            while True:
                line = input("Enter content line (or 'stop' to finish): ")
                if line == "stop":
                    break
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{timestamp}\n{line}\n")
        print(f"File '{filename}' created or updated.")
    except Exception as e:
        print(f"Error creating or updating file: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d <directory_path>] [-f <file_name>]")
        return

    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory_path = sys.argv[dir_index]
        filename = sys.argv[file_index]
        create_directory(directory_path)
        create_file(os.path.join(directory_path, filename))
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory_path = sys.argv[dir_index]
        create_directory(directory_path)
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]
        create_file(filename)
    else:
        print("Invalid arguments. Use -d for directory creation and -f for file creation.")


if __name__ == "__main__":
    main()
