import os
import sys
import datetime


def create_file() -> None:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    mode = None

    for arg in args:
        if arg == "-d":
            mode = "d"
        elif arg == "-f":
            mode = "f"
        elif mode == "d":
            dir_parts.append(arg)
        elif mode == "f":
            file_name = arg

    if dir_parts:
        path = os.path.join(*dir_parts)
        os.makedirs(path, exist_ok=True)

    if file_name:
        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        content_block = timestamp + "\n"
        for i, line in enumerate(lines, start=1):
            content_block += f"{i} {line}\n"

        if dir_parts:
            full_path = os.path.join(path, file_name)
        else:
            full_path = file_name

        if os.path.exists(full_path):
            content_block = "\n" + content_block

        with open(full_path, "a") as f:
            f.write(content_block)


create_file()
