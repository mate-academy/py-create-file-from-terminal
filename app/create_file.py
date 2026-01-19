import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d [directories] -f [file_name]")
        return

    directory = None
    file_name = None
    content_lines = []

    if "-d" in args:
        d_index = args.index("-d")
        try:
            f_index = args.index("-f")
        except ValueError:
            f_index = len(args)
        directory = os.path.join(*args[d_index + 1:f_index])

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if directory:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory created or already exists: {directory}")

    if file_name:
        if directory:
            file_path = os.path.join(directory, file_name)
        else:
            file_path = file_name

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Enter content line (type 'stop' to finish):")
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)

        with open(file_path, "a") as file:
            file.write(f"\n{timestamp}\n")
            for i, line in enumerate(content_lines, start=1):
                file.write(f"{i} {line}\n")

        print(f"File created or updated: {file_path}")
    else:
        if directory:
            print("Directory created successfully.")
        else:
            print("No file or directory operation specified.")


if __name__ == "__main__":
    create_file()
