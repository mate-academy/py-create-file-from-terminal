import os
import sys
from datetime import datetime
from typing import List, Optional


def create_file(directory: str, filename: str, content: List[str]) -> None:
    filepath = os.path.join(directory, filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(filepath):
        with open(filepath, "a") as file:
            file.write("\n\n" + timestamp + "\n")
            for line_number, line in enumerate(content, start=1):
                file.write(f"{line_number} {line}\n")
    else:
        with open(filepath, "w") as file:
            file.write(timestamp + "\n")
            for line_number, line in enumerate(content, start=1):
                file.write(f"{line_number} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    directory: Optional[str] = None
    filename: Optional[str] = None
    content: List[str] = []

    while args:
        flag = args.pop(0)
        if flag == "-d":
            directory = os.path.join(directory, args.pop(0)) \
                if directory else args.pop(0)
        elif flag == "-f":
            filename = args.pop(0)
        else:
            content.append(flag)

    if directory:
        os.makedirs(directory, exist_ok=True)

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    create_file(directory, filename, content)


if __name__ == "__main__":
    main()
