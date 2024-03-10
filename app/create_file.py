import os
import sys
from datetime import datetime


def create_file(directory, filename) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = []
    if os.path.exists(os.path.join(directory, filename)):
        with open(os.path.join(directory, filename), "r") as file:
            content = file.readline()
    else:
        content.append(timestamp + "\n")

    line_number = len(content) - 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        line_number += 1
        content.append(f"{line_number} {line}\n")

    with open(os.path.join(directory, filename), "w") as file:
        file.writelines(content)


def main() -> None:
    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[directory_index:])
        os.makedirs(directory, exist_ok=True)
        filename = None
    elif "-f" in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        filename = sys.argv[filename_index]
        directory = os.getcwd()
    else:
        print("Please specify either -d or -f flag.")
        return

    if filename:
        create_file(directory, filename)
        print(f"File {filename} created at {directory}")
    else:
        print(f"Directory {directory} created.")

    if __name__ == "__main__":
        main()

