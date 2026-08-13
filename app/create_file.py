import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    directories = []
    filename = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")

            if d_index < f_index:
                directories = args[d_index + 1:f_index]
            else:
                directories = args[d_index + 1:]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        filename = args[f_index + 1]

    if directories:
        directory = os.path.join(*directories)
        os.makedirs(directory, exist_ok=True)
    else:
        directory = "."

    if filename:
        file_path = os.path.join(directory, filename)

        lines = []

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        content = timestamp + "\n"

        for number, line in enumerate(lines, start=1):
            content += f"{number} {line}\n"

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            content = "\n" + content

        with open(file_path, "a", encoding="utf-8") as file:
            file.write(content)


main()
