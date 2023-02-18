import os
import sys
from datetime import datetime
from typing import List


def create_directory_and_file(path: List[str]) -> None:
    dirs_path, file_name = None, None

    if "-d" in path:
        directories = []
        for directory in path[path.index("-d") + 1:]:
            if directory == "-f":
                break
            directories.append(directory)
        dirs_path = os.path.join(*directories)
        os.makedirs(dirs_path, exist_ok=True)

    if "-f" in path:
        if dirs_path is None:
            file_name = path[path.index("-f") + 1]
        else:
            file_name = os.path.join(dirs_path, path[path.index("-f") + 1])
        open_type = "w" if not os.path.exists(file_name) else "a"
        with open(file_name, open_type) as file_in:
            file_in.write(
                f"{datetime.now().strftime('%Y-%m-%d %I:%M:%S')}\n"
            )
            line_number = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                file_in.write(f"{line_number} {content}\n")
                line_number += 1
            file_in.write("\n")


if __name__ == "__main__":
    cmd = sys.argv[1:]
    if "-d" in cmd or "-f" in cmd:
        create_directory_and_file(cmd)
