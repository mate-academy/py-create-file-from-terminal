import os
import sys
from datetime import datetime
from typing import List, Optional


def create_file(
        directory: List[str],
        filename: Optional[str],
        content: List[str]
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [f"{i} {line}" for i, line in enumerate(content, start=1)]

    if directory:
        path = os.path.join(*directory, filename)
    else:
        path = filename

    if os.path.exists(path):
        with open(path, "a") as file:
            file.write("\n\n" + timestamp + "\n" + "\n".join(lines))
    else:
        with open(path, "w") as file:
            file.write(timestamp + "\n" + "\n".join(lines))


def main() -> None:
    directory = []
    filename = None
    content = []

    for arg in sys.argv[1:]:
        if arg == "-d":
            directory_mode = True
        elif arg == "-f":
            directory_mode = False
        elif directory_mode:
            directory.append(arg)
        elif filename is None:
            filename = arg

    if directory:
        os.makedirs(os.path.join(*directory), exist_ok=True)

    if filename:
        print("Enter content line (type 'stop' to finish):")
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content.append(line)

        create_file(directory, filename, content)
        print(f"File '{filename}' created successfully!")


if __name__ == "__main__":
    main()
