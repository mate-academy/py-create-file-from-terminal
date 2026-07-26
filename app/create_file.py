import os
import argparse
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-f")
parser.add_argument("-d", nargs="*")

args = parser.parse_args()


def file_readactor(file_path: str) -> None:
    line_count = 1
    data_list = []
    while True:
        data_line = input("Enter content line: ")

        if data_line == "stop":
            break

        complete_line = f"{line_count} {data_line}"
        data_list.append(complete_line)
        line_count += 1
    file_mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, file_mode) as file:
        timestamp_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = timestamp_string + "\n" + "\n".join(data_list)
        file.write(line)


if args.f and args.d:
    os.makedirs(os.path.join(*args.d))
    filepath = os.path.join(*args.d, args.f)
    file_readactor(filepath)
elif args.d:
    os.makedirs(os.path.join(*args.d))
elif args.f:
    file_readactor(args.f)
