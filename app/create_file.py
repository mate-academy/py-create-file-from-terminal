import os
import sys
import datetime


def create_file(directory: str, filename: str) -> None:
    file_path = os.path.join(directory, filename)

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "w") as file:
            file.write(timestamp + "\n")

    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        with open(file_path, "a") as file:
            file.write(f"{line_number} {line}\n")
        line_number += 1


def create_dir(path_dir: list) -> None:
    path = os.path.join(*path_dir)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)


def main() -> None:
    info_from_terminal = sys.argv

    if "-d" in info_from_terminal and "-f" in info_from_terminal:
        index_d = info_from_terminal.index("-d")
        index_f = info_from_terminal.index("-f")

        if index_d < index_f:
            create_dir(info_from_terminal[index_d + 1: index_f])
            create_file(info_from_terminal[-1])
        else:
            create_dir(info_from_terminal[index_d + 1:])
            create_file(info_from_terminal[index_f + 1])

    elif "-d" in info_from_terminal:
        index_start = info_from_terminal.index("-d")
        create_dir(info_from_terminal[index_start + 1:])

    elif "-f" in info_from_terminal:
        create_file(info_from_terminal[1])


if __name__ == "__main__":
    main()
