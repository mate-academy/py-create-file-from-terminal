import argparse
import os
import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()
    if args.d:
        os.makedirs(os.path.join(*args.d), exist_ok=True)
    if args.f:
        file_path = args.f
        if args.d:
            file_path = os.path.join(*args.d, file_path)
        write_lines(file_path)


def write_lines(file_name: str) -> None:
    count = 0
    lines = []
    with open(file_name, "a") as file:
        if file.tell() > 0:
            file.write("\n")
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            count += 1
            lines.append(f"{count} {line}\n")
        file.writelines(lines)


create_file()
