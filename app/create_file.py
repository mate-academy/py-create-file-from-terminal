import os
import sys
from datetime import datetime


def read_arguments() -> tuple[str, str]:  # (path, filename)
    args = sys.argv[1:]
    if "-d" not in args and "-f" not in args:
        print("Usage: python create_file.py [-d directory] [-f filename]")
        print(args)
        exit()
    path, filename = None, None
    f_index, d_index = None, None

    if "-f" in args:
        f_index = args.index("-f") + 1
        filename = args[f_index]
    if "-d" in args:
        d_index = args.index("-d") + 1
        path = (
            os.path.join(*args[d_index: f_index])
            if f_index and d_index == 0 else
            os.path.join(*args[d_index:])
        )
    return path, filename


def input_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_data_to_file(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(timestamp + "\n")
        for idx, line in enumerate(content, start=1):
            file.write(f"{idx} {line}\n")


def main() -> None:
    path, filename = read_arguments()
    if path:
        os.makedirs(path, exist_ok=True)
    if filename:
        lines = input_lines()
        file_path = os.path.join(path, filename) if path else filename
        write_data_to_file(file_path=file_path, content=lines)


if __name__ == "__main__":
    main()
