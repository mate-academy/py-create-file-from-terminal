import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str, content: list) -> None:
    filepath = os.path.join(directory, filename)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}\n" + "\n".join(
        [f"{i} {line}" for i, line in enumerate(content, 1)]
    )
    if os.path.exists(filepath):
        with open(filepath, "a") as f:
            f.write("\n\n" + content)
    else:
        with open(filepath, "w") as f:
            f.write(content)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory = os.path.join(*sys.argv[dir_index : file_index - 1])
        filename = sys.argv[file_index]
        content = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content.append(line)
        create_file(directory, filename, content)
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        os.makedirs(directory, exist_ok=True)
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]
        content = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content.append(line)
        create_file(os.getcwd(), filename, content)


if __name__ == "__main__":
    main()
