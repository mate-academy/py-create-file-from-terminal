import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    directory_parts: list[str] = []
    filename: str | None = None
    current_flag: str | None = None

    for arg in args:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        elif current_flag == "-d":
            directory_parts.append(arg)
        elif current_flag == "-f":
            filename = arg

    directory = (
        os.path.join(*directory_parts)
        if directory_parts else "."
    )

    if directory_parts:
        os.makedirs(directory, exist_ok=True)

    if filename is None:
        return

    file_path = os.path.join(directory, filename)

    lines: list[str] = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = (
        os.path.isfile(file_path)
        and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        file.write(timestamp + "\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


main()
