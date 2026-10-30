import os
import sys
from datetime import datetime


arguments = sys.argv[1:]

directory_path = ""

if "-d" in arguments:
    directory_index = arguments.index("-d")

    if "-f" in arguments:
        file_index = arguments.index("-f")
        directories = arguments[directory_index + 1:file_index]
    else:
        directories = arguments[directory_index + 1:]

    directory_path = os.path.join(*directories)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

if "-f" in arguments:
    file_index = arguments.index("-f")
    file_name = arguments[file_index + 1]

    file_path = (
        os.path.join(directory_path, file_name)
        if directory_path
        else file_name
    )

    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = [timestamp]

    for index, line in enumerate(lines, start=1):
        content.append(f"{index} {line}")

    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")

        file.write("\n".join(content))
