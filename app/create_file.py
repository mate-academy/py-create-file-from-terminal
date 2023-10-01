import sys
import os
from datetime import datetime


def create_file(directory: str, filename: str, content: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_timestamp = f"{timestamp}\n{content}"
    file_path = os.path.join(directory, filename)

    os.makedirs(directory, exist_ok=True)

    with open(file_path, "a") as file:
        file.write(content_with_timestamp + "\n")


def main() -> None:
    directory = None
    filename = None

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-d" and i + 1 < len(sys.argv):
            directory = sys.argv[i + 1]
        elif sys.argv[i] == "-f" and i + 1 < len(sys.argv):
            filename = sys.argv[i + 1]

    if directory is None or filename is None:
        print("-d and -f")

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    content = "\n".join(content_lines)

    create_file(directory, filename, content)


if __name__ == "__main__":
    main()
