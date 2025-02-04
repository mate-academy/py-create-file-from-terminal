import os
import sys
from datetime import datetime


def create_file() -> str:
    dir_path = ""
    file_name = ""

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        while (dir_index < len(sys.argv)
               and not sys.argv[dir_index].startswith("-")):
            dir_path = os.path.join(dir_path, sys.argv[dir_index])
            dir_index += 1

    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name
    else:
        print("Please provide either -d or -f flag.")
        return

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        line_number = 1
        while True:
            content_line = input(f"Enter content line {line_number}: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{line_number} {content_line}\n")
            line_number += 1

    print(f"File '{file_path}' created/updated successfully.")


if __name__ == "__main__":
    create_file()
