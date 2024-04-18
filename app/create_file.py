import sys
import os
from datetime import datetime


def create_file(file_path: str, content: str) -> None:
    with open(file_path, "a") as file:
        file.write(content)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py <-d dir1 dir2> <-f file.txt>")
        return

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dir_path = os.path.join(*sys.argv[dir_index:])
        if "-f" not in sys.argv:
            os.makedirs(dir_path, exist_ok=True)
            return
        else:
            dir_path = os.path.join(*sys.argv[dir_index:-2])
        file_path = os.path.join(dir_path, sys.argv[-1])

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_path = sys.argv[file_index]

    print("Enter content line (type 'stop' to finish):")
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    content = "\n".join(content_lines)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content_with_timestamp = f"{timestamp}\n{content}\n"

    create_file(file_path, content_with_timestamp)
    print(f"{file_path}")


if __name__ == "__main__":
    main()
