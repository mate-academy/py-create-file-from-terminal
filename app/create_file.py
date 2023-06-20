import os
import sys
from datetime import datetime


def create_file(directory: str, file_name: str) -> None:
    file_path = os.path.join(directory, file_name)
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.readlines()

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)

    with open(file_name, "w") as f:
        f.write(time_stamp + "\n")
        for i, line in enumerate(content, start=1):
            f.write(f"{i} {line}\n")

    print(f"File {file_name} created in {file_path}")


def create_directory(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)
    print(f"Directory {directory} created")


def main() -> None:
    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[directory_index:])
        create_directory(directory)
    elif "-f" in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        filename = sys.argv[filename_index]
        create_file(os.getcwd(), filename)
    elif "-d" in sys.argv and "-f" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[directory_index:-2])
        filename_index = sys.argv.index("-f") + 1
        filename = sys.argv[filename_index]
        create_directory(directory)
        create_file(directory, filename)
    else:
        print("Wrong command")


if __name__ == "__main__":
    main()
