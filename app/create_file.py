import sys
import os
from datetime import datetime


def validate_file_name(name: str) -> None:
    if not name or name.count(".") != 1:
        raise ValueError("File should include only one dot")


def write_content(file_path_name: str) -> None:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines_to_append = []

    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        lines_to_append.append(text)

    final_lines = []

    if os.path.exists(file_path_name) and os.path.getsize(file_path_name) > 0:
        final_lines.append("\n")

    final_lines.append(f"{current_date}\n")

    for index, line in enumerate(lines_to_append, start=1):
        final_lines.append(f"{index} {line}\n")

    with open(file_path_name, "a") as file:
        file.writelines(final_lines)


try:
    arguments = sys.argv
    dir_parts = []
    file_name = None
    collecting_dirs = False

    i = 0
    while i < len(arguments):
        arg = arguments[i]

        if arg.endswith(".py"):
            i += 1
            continue

        if arg == "-d":
            collecting_dirs = True
            i += 1
            continue

        if arg == "-f":
            collecting_dirs = False
            if i + 1 < len(arguments):
                file_name = arguments[i + 1]
                i += 2
            else:
                i += 1
            continue

        if collecting_dirs:
            dir_parts.append(arg)

        i += 1

    if file_name:
        validate_file_name(file_name)

    if dir_parts:
        path = os.path.join(os.getcwd(), *dir_parts)
        os.makedirs(path, exist_ok=True)
        if file_name:
            file_path = os.path.join(path, file_name)
            write_content(file_path)
    elif file_name:
        file_path = os.path.join(os.getcwd(), file_name)
        write_content(file_path)

except ValueError as error:
    print(error)
