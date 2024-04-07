import os
import sys
from datetime import datetime

def create_directory(path: str) -> None:
    try:
        os.makedirs(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")

def create_file_with_content(file_path: str, content: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_numbers = [
        f"{i} {line}" for i, line in enumerate(content, start=1)
    ]
    content_with_numbers.insert(0, timestamp)

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        file.write("\n".join(content_with_numbers) + "\n" * 2)

    if mode == "w":
        print(f"File '{file_path}' created with content.")
    else:
        print(f"File '{file_path}' has been appended with content.")

def main() -> None:
    args = sys.argv[1:]

    if not args or ("-d" not in args and "-f" not in args):
        print(
            "Usage: python create_file.py -d [directory_path] "
            "or -f [file_path]"
        )
        return

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d") + 1
        file_index = args.index("-f") + 1

        directory_path = os.path.join(*args[dir_index:file_index - 1])
        file_path = os.path.join(directory_path, args[file_index])

        create_directory(directory_path)
        content = []
    elif "-d" in args:
        dir_index = args.index("-d") + 1
        directory_path = os.path.join(*args[dir_index:])

        create_directory(directory_path)
        return
    else:
        file_index = args.index("-f") + 1
        file_path = args[file_index]
        content = []

    if content is not None:
        print("Enter content lines (type 'stop' to finish):")
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content.append(line)

        create_file_with_content(file_path, content)

if __name__ == "__main__":
    main()
