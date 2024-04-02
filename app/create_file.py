import os
import sys
from datetime import datetime


def create_file(
        directory: str,
        filename: str,
        content_lines: list[str]
) -> None:
    filepath = os.path.join(directory, filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i} {line}"
                      for i, line in enumerate(content_lines, start=1)]
    content = f"{timestamp}\n" + "\n".join(numbered_lines)

    if os.path.exists(filepath):
        with open(filepath, "a") as file:
            file.write("\n\n" + content)
    else:
        with open(filepath, "w") as file:
            file.write(content)


def main() -> None:
    directory = None
    filename = None
    content_lines = []

    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[directory_index:])
        os.makedirs(directory, exist_ok=True)

    if "-f" in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        filename = sys.argv[filename_index]

    if not directory and not filename:
        print("Please provide either -d or -f flag.")
        return

    if filename:
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)
        create_file(directory, filename, content_lines)


if __name__ == "__main__":
    main()
