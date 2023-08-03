import os
import sys
from datetime import datetime
from typing import Any


def create_file_with_content(file_path: str) -> Any:
    content_line = []
    while True:
        input_line = input("Enter content line:")

        if input_line == "stop":
            break
        content_line.append(input_line)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_w_time = f"{current_time}"

    for i, content in enumerate(content_line):
        content = f"\n{i + 1}" + f"\t{content}"
        content_w_time += content

    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("".join(content_w_time))
    else:
        with open(file_path, "a") as file:
            file.write("".join(content_w_time))


def main() -> Any:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        dir_path = os.path.join(*sys.argv[dir_index:file_index - 1])
        file_name = sys.argv[file_index]
        file_path = os.path.join(dir_path, file_name)
        os.makedirs(dir_path, exist_ok=True)
        create_file_with_content(file_path)

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dir_path = os.path.join(*sys.argv[dir_index:])
        os.makedirs(dir_path, exist_ok=True)

    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_path = sys.argv[file_index]
        create_file_with_content(file_path)


if __name__ == "__main__":
    main()
