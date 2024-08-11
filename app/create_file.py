import os
import sys
from datetime import datetime

list_args = sys.argv


def write_file(path: str) -> None:
    with open(path, "w") as file:
        now = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        index = 1
        file.write(now)
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"\n{index} Line {content}")
            index += 1


if "-d" in list_args and "-f" in list_args:
    file_index = list_args.index("-f")
    dirs_list = list_args[list_args.index("-d") + 1:file_index]
    dirs_path = os.path.join(*dirs_list)
    os.makedirs(dirs_path, exist_ok=True)
    file_name = list_args[file_index + 1]
    file_path = os.path.join(dirs_path, file_name)
    write_file(path=file_path)

elif "-f" in list_args:
    file_path = list_args[-1]
    write_file(path=file_path)

elif "-d" in list_args:
    dirs_list = list_args[list_args.index("-d") + 1:]
    dirs_path = os.path.join(*dirs_list)
    os.makedirs(dirs_path, exist_ok=True)
