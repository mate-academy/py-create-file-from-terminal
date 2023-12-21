import os
import sys
from datetime import datetime


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def create_file(file_path: str, content_lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [
        f"{counter + 1} {line}" for counter, line in enumerate(content_lines)
    ]

    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"

    with open(file_path, "a" if os.path.exists(file_path) else "w") as file:
        if mode == "a":
            file.write(f"\n\n{timestamp}\n")
            file.write("\n".join(content))
        elif mode == "w":
            file.write(f"{timestamp}\n")
            file.write("\n".join(content))


def main() -> None:
    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory_path_list = sys.argv[directory_index:]
        directory_path = os.path.join(
            *directory_path_list[:directory_path_list.index("-f")]
            if "-f" in directory_path_list else directory_path_list
        )
        create_directory(directory_path)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        file_path = (os.path.join(directory_path, file_name)
                     if "-d" in sys.argv else file_name)

        content_lines = []
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            content_lines.append(content_line)

        create_file(file_path, content_lines)


if __name__ == "__main__":
    main()
