import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    append_content = "a" if os.path.exists(file_path) else "w"

    with open(file_path, append_content) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created.")


def main() -> None:
    args = sys.argv
    directory: str | None = None

    if "-d" in args:
        index_ = args.index("-d") + 1
        directory = os.path.join(*args[index_:])
        create_directory(directory)

    if "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        file_path = os.path.join(directory or "", file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
