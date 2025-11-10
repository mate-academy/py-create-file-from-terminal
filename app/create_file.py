import sys
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    dir_list = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_list = args[d_index + 1: f_index]
        else:
            dir_list = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return dir_list, file_name


def create_directories(dir_list: list[str], file_name: str | None) -> str:
    if dir_list:
        path = os.path.join(*dir_list)
        os.makedirs(path, exist_ok=True)
        print(f"Directories created: {path}")
    else:
        path = ""

    if file_name:
        file_path = os.path.join(path, file_name) if path else file_name
        return file_path
    else:
        return path


def write_file(file_path: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    if not lines:
        print("There is no content. File was not changed.")
        return

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(timestamp + "\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")
        file.write("\n")

    print(f"File '{file_path}' updated with {len(lines)} lines.")


if __name__ == "__main__":
    dir_list, file_name = parse_arguments()
    file_path = create_directories(dir_list, file_name)
    if file_name:
        write_file(file_path)
    else:
        print("No file name was provided (-f). "
              "Only directory(ies) were created.")
