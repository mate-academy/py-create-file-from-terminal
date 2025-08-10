import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        file.write(timestamp + "\n")

        line_number = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line_content}\n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        filename_index = sys.argv.index("-f") + 1
        if directory_index < filename_index:
            directory_path = os.path.join(
                *sys.argv[directory_index:filename_index - 1])

        else:
            directory_path = os.path.join(
                *sys.argv[directory_index:])

        filename = sys.argv[filename_index]
        os.makedirs(directory_path, exist_ok=True)

        file_path = os.path.join(directory_path, filename)
        create_file(file_path)

    elif "-f" in sys.argv and "-d" not in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        filename = sys.argv[filename_index]

        create_file(filename)

    elif "-d" in sys.argv and "-f" not in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory_path = os.path.join(*sys.argv[directory_index:])
        os.makedirs(directory_path, exist_ok=True)


if __name__ == "__main__":
    main()
