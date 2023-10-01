import sys
import os
from datetime import datetime


def create_file(directory: str, filename: str, content: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_timestamp = f"{timestamp}\n{content}"

    file_path = os.path.join(directory, filename)

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n + content_with_timestamp")
    else:
        os.makedirs(directory, exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content_with_timestamp)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory = os.path.join(*sys.argv[dir_index:file_index])
        filename = sys.argv[file_index]
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        filename = input("Enter file name: ")
    elif "-f" in sys.argv:
        filename = sys.argv[sys.argv.index("-f") + 1]
        directory = input("Enter directory path: ")
    else:
        print("Use -d and/or -f flags")
        return

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    content = "\n".join(
        f"{i}. {line}" for i, line in enumerate(content_lines, start=1)
    )

    create_file(directory, filename, content)


if __name__ == "__main__":
    main()
