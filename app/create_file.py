import os
import sys
from datetime import datetime


def get_content() -> str:
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

    return "\n".join(content) + "\n"


def main() -> None:
    args = sys.argv[1:]

    directory = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")

            if d_index < f_index:
                dirs = args[d_index + 1:f_index]
            else:
                dirs = args[d_index + 1:]
        else:
            dirs = args[d_index + 1:]

        if dirs:
            directory = os.path.join(*dirs)
            os.makedirs(directory, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

        content = get_content()

        file_path = (
            os.path.join(directory, file_name)
            if directory
            else file_name
        )

        with open(file_path, "a", encoding="utf-8") as file:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                file.write("\n")
            file.write(content)


main()
