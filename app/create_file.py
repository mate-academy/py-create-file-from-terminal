from datetime import datetime

import os

import argparse


def create_dir(dir_name: list[str]) -> None:
    path = os.path.join(*dir_name)
    os.makedirs(path, exist_ok=True)


def create_file(file_name: str,
                content: list[str],
                dir_name: str = "") -> None:
    path = os.path.join(*dir_name, file_name)
    with open(path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in content:
            f.write(f"{line}\n")


def write_content() -> list[str]:
    result_input = []
    line_num = 1
    while True:
        content = input(f"Enter content line {line_num}: ")
        if content.lower() == "stop":
            break
        result_input.append(f"{line_num} {content}")
        line_num += 1
    return result_input


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
                        "--directory",
                        help="Directory path",
                        nargs="+",
                        default="")
    parser.add_argument("-f",
                        "--filename",
                        help="File name",
                        default="")

    args = parser.parse_args()

    dir_paths = args.directory
    file_name = args.filename

    if dir_paths:
        create_dir(dir_paths)

    if file_name:
        input_data = write_content()
        create_file(file_name, input_data, dir_paths)


if __name__ == "__main__":
    main()
