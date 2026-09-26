import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    directory_parts = []
    file_name = None
    current_flag = None

    for arg in args:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        elif current_flag == "-d":
            directory_parts.append(arg)
        elif current_flag == "-f" and file_name is None:
            file_name = arg

    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)
    if file_name is None:
        return

    if directory_parts:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_has_content = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as file:
        if file_has_content:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for number, line in enumerate(content_lines, start=1):
            file.write(f"{number} {line}\n")


main()
