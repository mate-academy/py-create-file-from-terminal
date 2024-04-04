import os
import sys
from datetime import datetime


def create_file(
        file_path: list[str] | str,
        content_lines: list[str] | str
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [f"{timestamp}"] + [
        f"{i} {line}" for i, line in enumerate(content_lines, 1)
    ]
    with open(file_path, "a" if os.path.exists(file_path) else "w") as file:
        file.write("\n".join(content) + "\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(
            "Usage: python create_file.py [-d directory_path] [-f file_name]"
        )
        return

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d") + 1
        file_index = args.index("-f") + 1
        directory_path = os.path.join(*args[dir_index:file_index - 1])
        file_name = args[file_index]

        os.makedirs(directory_path, exist_ok=True)
        file_path = os.path.join(directory_path, file_name)

        content_lines = []
        print("Enter content line (input 'stop' to finish):")
        while True:
            line = input()
            if line.strip() == "stop":
                break
            content_lines.append(line)

        create_file(file_path, content_lines)
        print(f"File '{file_name}' created in directory '{directory_path}'.")

    elif "-d" in args:
        dir_index = args.index("-d") + 1
        directory_path = os.path.join(*args[dir_index:])
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory '{directory_path}' created.")

    elif "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        file_path = os.path.join(os.getcwd(), file_name)

        content_lines = []
        print("Enter content line (input 'stop' to finish):")
        while True:
            line = input()
            if line.strip() == "stop":
                break
            content_lines.append(line)

        create_file(file_path, content_lines)
        print(f"File '{file_name}' created in current directory.")


if __name__ == "__main__":
    main()
