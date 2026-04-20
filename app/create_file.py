import os
import sys
import datetime


directories = []
filename = None


for i in range(len(sys.argv)):
    if sys.argv[i] == "-d":
        next_step = i + 1
        while next_step < len(sys.argv) and sys.argv[next_step] != "-f":
            if sys.argv[next_step].startswith("-"):
                break
            directories.append(sys.argv[next_step])
            next_step += 1
    if sys.argv[i] == "-f":
        filename = sys.argv[i + 1] if i + 1 < len(sys.argv) else None


def create_directories() -> str:
    path = os.path.join(".", *directories)
    abs_path = os.path.abspath(path)
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
    return abs_path


def get_content_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, content: list[str]) -> None:
    if not content:
        return

    has_content = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a") as source_file:
        if has_content:
            source_file.write("\n")
        source_file.write(f"{datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )}\n")
        for index, line in enumerate(content, start=1):
            source_file.write(f"{index} {line}\n")


def create_file(filename: str) -> None:
    if directories:
        dir_path = create_directories()
    else:
        dir_path = os.getcwd()

    file_path = os.path.join(dir_path, filename)
    lines = get_content_lines()
    write_to_file(file_path, lines)


if __name__ == "__main__":
    if filename:
        create_file(filename)
    elif directories:
        create_directories()
        print("Directories created. No file specified.")
    else:
        print("No filename given")
        sys.exit(1)
