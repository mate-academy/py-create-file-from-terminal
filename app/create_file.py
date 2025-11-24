import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv

    directory = None
    file_name = None
    full_path = None

    if "-d" in args:
        try:
            directory = args[args.index("-d") + 1]
        except IndexError:
            print("Error: -d flag requires a directory name.")
            sys.exit(1)

    if "-f" in args:
        try:
            file_name = args[args.index("-f") + 1]
        except IndexError:
            print("Error: -f flag requires a file name.")
            sys.exit(1)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if directory and file_name:
        os.makedirs(directory, exist_ok=True)
        full_path = os.path.join(directory, file_name)
        if not os.path.exists(full_path):
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(timestamp + "\n")
        print(f"Directory created: {directory}")
        print(f"File created inside directory: {full_path}")

    elif directory:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory created: {directory}")

    elif file_name:
        full_path = file_name
        if not os.path.exists(full_path):
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(timestamp + "\n")

        print(f"File created: {full_path}")

    else:
        print("Usage: python create.py -d <dir> -f <file>")
        return

    if full_path is None:
        print("No file to write content. Only directory was created.")
        return

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(full_path, "a", encoding="utf-8") as f:
        for i, text in enumerate(lines, start=1):
            f.write(f"{i}. {text}\n")
        f.write("\n")

    print(f"Content added to {full_path}")


if __name__ == "__main__":
    create_file()
