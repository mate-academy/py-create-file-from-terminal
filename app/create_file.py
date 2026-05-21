import sys
import os
import datetime


def create_file() -> None:
    args = sys.argv[1:]

    file_name = args[args.index("-f") + 1] if "-f" in args else None

    if "-d" in args:
        d_index = args.index("-d")
        folders = [a for a in args[d_index + 1:]
                   if not a.startswith("-") and a != file_name]
        os.makedirs(os.path.join(*folders), exist_ok=True)
    else:
        folders = []

    if not file_name:
        return

    file_path = os.path.join(*folders, file_name) if folders else file_name

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(f"{now}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1


create_file()
