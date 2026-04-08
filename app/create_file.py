import sys
from datetime import datetime
import os


def create_file_from_console() -> None:
    arguments = sys.argv
    folder_parts = []
    file_name = ""
    target_path = os.getcwd()

    if "-d" in arguments:
        for item in arguments[arguments.index("-d") + 1:]:
            if item.startswith("-"):
                break
            folder_parts.append(item)

    if "-f" in arguments:
        file_name = arguments[arguments.index("-f") + 1]

    if folder_parts:
        target_path = os.path.join(target_path, *folder_parts)
        os.makedirs(target_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(target_path, file_name)

        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content_lines.append(line)

        needs_separator = (os.path.exists(file_path)
                           and os.path.getsize(file_path) > 0)

        with open(file_path, "a") as f:
            if needs_separator:
                f.write("\n")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")
            for index, line in enumerate(content_lines, start=1):
                f.write(f"{index} {line}\n")


if __name__ == "__main__":
    create_file_from_console()
