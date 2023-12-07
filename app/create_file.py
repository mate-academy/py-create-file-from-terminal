import sys
import os
from datetime import datetime


def create_content(file_name: str) -> None:
    if os.path.exists(file_name):
        with (open(file_name, "a") as file):
            file.write("\n\n")

    content = ""
    line_number = 1

    while True:
        line = input("Enter content line -> ")
        if line == "stop":
            break
        content += str(line_number) + " " + line + "\n"
        line_number += 1

    if content:
        with (open(file_name, "a") as file):
            content = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S") + "\n" + content
            file.write(content.rstrip())


if __name__ == "__main__":
    arguments = sys.argv

    f_index = d_index = None
    if "-d" in arguments:
        d_index = arguments.index("-d")
    if "-f" in arguments:
        f_index = arguments.index("-f")

    if f_index and d_index:
        if arguments[1] == "-f":
            f_command = arguments[2:d_index]
            d_command = os.path.join(*arguments[d_index + 1:])
        else:
            d_command = os.path.join(*arguments[2:f_index])
            f_command = arguments[f_index + 1:]
        if len(f_command) > 1:
            raise SystemExit(
                "use '-f file_name' format to create and write to a file"
            )
        os.makedirs(d_command, exist_ok=True)
        create_content(os.path.join(d_command, arguments[f_index + 1]))
    elif d_index:
        d_command = os.path.join(*arguments[2:])
        os.makedirs(d_command, exist_ok=True)
    else:
        if len(arguments) > 3:
            raise SystemExit(
                "use '-f file_name' format to create and write to a file")
        create_content(arguments[2])
