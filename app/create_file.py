import os
import sys
from datetime import datetime
from typing import Any

def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d <directories> -f <filename>")
        return

    directory_path = []
    file_name = None

    if '-d' in args:
        dir_index = args.index('-d')
        for i in range(dir_index + 1, len(args)):
            if args[i] == '-f':
                break
            directory_path.append(args[i])

    if '-f' in args:
        file_index = args.index('-f')
        if file_index + 1 < len(args):
            file_name = args[file_index + 1]

    if directory_path:
        full_path = os.path.join(*map(str, directory_path))
        os.makedirs(full_path, exist_ok=True)
    else:
        full_path = os.getcwd()

    if file_name:
        file_path = os.path.join(str(full_path), str(file_name))
        append_content_to_file(file_path)
    else:
        print("No file specified. Only directories created.")


def append_content_to_file(file_path: Any) -> None:
    print(f"Creating or appending content to: {file_path}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    if not content_lines:
        print("No content provided. File not modified.")
        return

    formatted_content = [f"{i + 1} {line}" for i, line in enumerate(content_lines)]
    content_to_write = f"\n{timestamp}\n" + "\n".join(formatted_content)

    with open(file_path, "a") as file:
        file.write(content_to_write)
        file.write("\n")

    print(f"Content written to {file_path}")


if __name__ == "__main__":
    main()
