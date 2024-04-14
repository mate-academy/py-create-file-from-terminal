import sys
import os
from datetime import datetime
from typing import List


def create_file(directory_path: str, file_name: str, lines: List[str]) -> None:
    file_path = os.path.join(directory_path, file_name)
    content = [f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]
    content.extend([f"{i+1} {line}" for i, line in enumerate(lines)])

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        file.write("\n".join(content) + "\n\n")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        index_d = args.index("-d")
        index_f = args.index("-f")
        directory_path = os.path.join(*args[index_d + 1:index_f])
        file_name = args[index_f + 1]
        lines = []
        print("Enter content line: ")
        while True:
            line = input()
            if line.lower() == "stop":
                break
            lines.append(line)
        os.makedirs(directory_path, exist_ok=True)
        create_file(directory_path, file_name, lines)
        print(f"Creates directory {directory_path} and "
              f"file {file_name} inside that directory with content:")
        print(os.path.join(directory_path, file_name))
        print("\n".join(lines))
    elif "-d" in args:
        index_d = args.index("-d")
        directory_path = os.path.join(*args[index_d + 1:])
        os.makedirs(directory_path, exist_ok=True)
        print(f"Created directory {directory_path}.")
    elif "-f" in args:
        index_f = args.index("-f")
        file_name = args[index_f + 1]
        lines = []
        print("Enter content line: ")
        while True:
            line = input()
            if line.lower() == "stop":
                break
            lines.append(line)
        create_file(os.getcwd(), file_name, lines)
        print(f"File {file_name} created with content:")
        print("\n".join(lines))
    else:
        print("No flags provided.")


if __name__ == "__main__":
    main()
