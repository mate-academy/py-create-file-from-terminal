import os
import sys
from datetime import datetime


def get_timestamp() -> datetime:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_file(file_path: str, content_lines: int) -> None:
    with open(file_path, "a") as file:
        file.write("\n".join(content_lines))


def main() -> None:
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory_path = os.path.join(*sys.argv[dir_index:])
        os.makedirs(directory_path, exist_ok=True)
        os.chdir(directory_path)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        file_path = os.path.join(os.getcwd(), file_name)

        if os.path.exists(file_path):
            with open(file_path, "r") as existing_file:
                content = existing_file.read().strip().split("\n")
        else:
            content = []

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content.append(line)

        content_with_timestamp = [get_timestamp()] + [
            f"{i + 1} {line}" for i, line in enumerate(content)
        ]
        create_file(file_path, content_with_timestamp)

        formatted_content = "\n".join(content_with_timestamp)
        formatted_content = formatted_content.replace("\\", "\\\\")
        print(f"File {file_path} created with content:\n\n{formatted_content}")


if __name__ == "__main__":
    main()
