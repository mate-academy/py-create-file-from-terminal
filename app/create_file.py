from datetime import datetime
import os
import sys


def create_file(file_name: str) -> None:
    with open(sys.argv[-1], "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date}\n")

        current_line = 1
        inline_content = input("Enter content line: ")

        while inline_content != "stop":
            file.write(f"Line{current_line} {inline_content}\n")
            inline_content = input("Enter content line: ")
            current_line += 1


def create_folder() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        folders = os.path.join(*sys.argv[2:sys.argv.index("-f")])
        os.makedirs(folders)
        create_file(os.path.join(folders, sys.argv[-1]))

    elif "-d" in sys.argv and len(sys.argv) > 2:
        folders = os.path.join(*sys.argv[2:])
        os.makedirs(folders)

    elif "-f" in sys.argv and len(sys.argv) > 2:
        create_file(sys.argv[-1])


if __name__ == "__main__":
    create_folder()
