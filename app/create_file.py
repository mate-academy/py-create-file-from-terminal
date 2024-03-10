import os
import sys
from datetime import datetime


def create_file(path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as file:
        file.write(timestamp + "\n")
        line_count = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            line_count += 1
            file.write(f"{line_count} {content}\n")
        file.write("\n")


def finding_path() -> None:
    args = sys.argv
    directory_path = ""
    file_name = ""

    if "-d" in args:
        dir_index = args.index("-d") + 1
        next_flag_index = (len(args) if "-f" not in args else args.index("-f"))
        directory_path_parts = args[dir_index:next_flag_index]
        directory_path = os.path.join(*directory_path_parts)
        if directory_path:
            os.makedirs(directory_path, exist_ok=True)

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index < len(args):
            file_name = args[file_index]
            file_path = (os.path.join(directory_path, file_name)
                         if directory_path else file_name)
            create_file(file_path)


if __name__ == "__main__":
    finding_path()
