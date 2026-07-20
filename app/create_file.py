import os
import sys
from datetime import datetime


def write_content(filepath: str) -> None:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        lines.append(user_input)

    file_exists_with_content = (os.path.exists(filepath)
                                and os.path.getsize(filepath) > 0)

    with open(filepath, "a") as f:
        if file_exists_with_content:
            f.write("\n")
        f.write(timestamp + "\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")


if "-d" in sys.argv and "-f" in sys.argv:
    d_index = sys.argv.index("-d")
    f_index = sys.argv.index("-f")

    if d_index < f_index:
        folders = sys.argv[d_index + 1:f_index]
    else:
        folders = sys.argv[d_index + 1:]

    file_name = sys.argv[f_index + 1]

    dir_path = os.path.join(*folders)
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, file_name)
    write_content(file_path)

elif "-d" in sys.argv:
    index = sys.argv.index("-d")
    folders = sys.argv[index + 1:]
    os.makedirs(os.path.join(*folders), exist_ok=True)

elif "-f" in sys.argv:
    index = sys.argv.index("-f")
    file_name = sys.argv[index + 1]
    write_content(file_name)
