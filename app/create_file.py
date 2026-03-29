import os
import sys
from datetime import datetime
from typing import List


def get_timestamp() -> str:
    return datetime.now().strftime("\n%Y-%m-%d %H:%M:%S")


def parse_arguments() -> str:
    dir_flag = "-d" in sys.argv
    file_flag = "-f" in sys.argv

    if not (dir_flag or file_flag):
        print("Please provide either the -d flag or the -f flag.")
        sys.exit(1)

    if dir_flag:
        dir_index = sys.argv.index("-d") + 1
        file_index = (
            sys.argv.index("-f")
            if "-f" in sys.argv
            else len(sys.argv)
        )

        if dir_index > file_index:
            dir_index, file_index = file_index, dir_index

        directory_path = os.path.join(*sys.argv[dir_index:file_index])
        os.makedirs(directory_path, exist_ok=True)
        os.chdir(directory_path)

    if file_flag:
        file_index = sys.argv.index("-f") + 1
        if dir_flag and file_index < dir_index:
            file_name = os.path.join(*sys.argv[file_index:dir_index])
        else:
            file_name = sys.argv[file_index]

        file_path = os.path.join(os.getcwd(), file_name)
        return file_path


def input_content() -> List[str]:
    content: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)
    return content


def format_content(content: List[str]) -> List[str]:
    return [f"{i + 1} {line}" for i, line in enumerate(content)]


def create_file(file_path: str, content_lines: List[str]) -> None:
    with open(file_path, "a") as file:
        file.write("\n".join(content_lines))


def main() -> None:
    file_path = parse_arguments()
    content = input_content()
    content_with_timestamp = [get_timestamp()] + format_content(content)
    create_file(file_path, content_with_timestamp)


if __name__ == "__main__":
    main()
