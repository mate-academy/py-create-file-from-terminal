import sys

# import os
from pathlib import Path
from datetime import datetime


def validation(arguments: list) -> None:
    if "-f" not in arguments:
        raise ValueError("-f parameter expected")
    if arguments[-1] == "-f":
        raise ValueError("Name of file expected")
    if arguments.count("-f") > 1:
        raise ValueError("So many -f arguments")

    if arguments[1] not in ["-f", "-d"]:
        raise ValueError("first parameter should be -f or -d")

    if "-d" in arguments:
        if arguments[1] != "-d":
            raise ValueError("expected argument -d out of range")
        if arguments[2] == "-f":
            raise ValueError("Expected directory name after -d")
        if arguments.count("-d") > 1:
            raise ValueError("So many -d arguments")


def create_folders(arguments: list) -> Path:
    path = Path()
    for i in range(arguments.index("-d") + 1, arguments.index("-f")):
        path = path / arguments[i]
        path.mkdir(exist_ok=True)
    return path


def color_text(text: str, color_code: str) -> str:
    return f"\033[{color_code}m{text}\033[0m"


def get_date() -> str:
    now = datetime.now()
    # format to 2022-02-01 14:41:10
    return now.strftime("%Y-%m-%d %H:%M:%S")


def input_lines() -> str:
    text = ""
    count = 1
    while True:
        new_line = input(f"{color_text('Enter', '33')} content line:")
        if new_line.lower() == "stop":
            break
        text += f"{color_text(str(count), '34')} "
        text += f"{color_text("Line" + str(count), '33')} {new_line}\n"
        count += 1
    return text


def main() -> None:
    validation(sys.argv)
    text = input_lines()
    arguments = sys.argv
    path = Path()
    if "-d" in arguments:
        path = create_folders(arguments)
    path = path / arguments[-1]
    now = color_text(get_date(), "34")
    output_text = f"{now} \n"
    output_text += f"{text}\n"
    print(output_text)
    output_file = open(path, "a")
    output_file.write(output_text)
    output_file.close()


if __name__ == "__main__":
    main()
