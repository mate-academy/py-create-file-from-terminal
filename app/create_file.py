import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            file.write(f"{line} {user_input}\n")
            line += 1

    print(f"File created/updated, {file_path}")


def main() -> None:
    args = sys.argv
    path = ""
    file_name = ""

    if len(args) < 3:
        print("Usage: python create_file.py -d [directories] or -f [filename]")
        return

    if "-d" in args:
        idx = args.index("-d")
        for i in range(idx + 1, len(args)):
            if args[i] == "-f":
                break
            path = os.path.join(path, args[i])

    if "-f" in args:
        idx = args.index("-f")
        if idx + 1 < len(args):
            file_name = args[idx + 1]

    if path and not file_name:
        create_directory(path)

    if file_name and not path:
        create_file(file_name)

    if path and file_name:
        create_directory(path)
        create_file(os.path.join(path, file_name))


if __name__ == "__main__":
    main()
