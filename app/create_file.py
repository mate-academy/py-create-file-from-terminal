import os
import sys
from datetime import datetime


def parse_args() -> tuple:
    d_index = sys.argv.index("-d") if "-d" in sys.argv else None
    f_index = sys.argv.index("-f") if "-f" in sys.argv else None
    return d_index, f_index


def create_directory_structure(
        d_index: int | None,
        f_index: int | None) -> any:
    dir_path = ""
    if d_index is not None:
        dirs = []
        i = d_index + 1

        while i < len(sys.argv):
            arg = sys.argv[i]
            if arg.startswith("-"):
                break
            if f_index is not None and i == f_index + 1:
                break
            dirs.append(arg)
            i += 1

        if dirs:
            dir_path = os.path.join(*dirs)
            os.makedirs(dir_path, exist_ok=True)
    return dir_path


def get_file_content() -> str:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_text = timestamp + "\n"
    for i, line in enumerate(lines, 1):
        output_text += f"{i} {line}\n"
    return output_text


def write_to_file(file_path: str, output_text: str) -> None:
    already_exists = os.path.exists(file_path)
    with open(file_path, "a", encoding="utf-8") as file:
        if already_exists:
            file.write("\n")
        file.write(output_text)


def main() -> None:
    d_index, f_index = parse_args()
    dir_path = create_directory_structure(d_index, f_index)

    if f_index is None or f_index + 1 >= len(sys.argv):
        return

    file_name = sys.argv[f_index + 1]
    file_path = os.path.join(dir_path, file_name)
    output_text = get_file_content()
    write_to_file(file_path, output_text)


main()
