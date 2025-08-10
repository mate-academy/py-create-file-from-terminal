import sys
import os
from datetime import datetime


def create_dir(path_parts: list) -> None:
    dir_path = os.path.join(*path_parts)
    os.makedirs(dir_path, exist_ok=True)


def create_file(file_name: str) -> None:
    content = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_timestamp = [
        f"{timestamp}\n",
        *[f"{i + 1} {line}\n" for i, line in enumerate(content)]
    ]

    with open(file_name, "a" if os.path.exists(file_name) else "w") as file:
        file.write("\n".join(content_with_timestamp))


def main() -> None:
    if len(sys.argv) < 3:
        raise ValueError("Usage: python create_file.py "
                         "-d <directory_path_parts> -f <file_name>")

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        create_dir(sys.argv[dir_index:sys.argv.index("-f")]
                   if "-f" in sys.argv else sys.argv[dir_index:])

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        create_file(sys.argv[file_index])


if __name__ == "__main__":
    main()
