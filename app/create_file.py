import argparse
import os
from datetime import datetime


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="CreateFile",
        description="takes directory path, "
                    "file name, file content from the terminal "
                    "and creates file. "
                    "There should be flag -d before direction "
                    "where file should be stored "
                    "and -f before name of the new file",
        epilog="print your command")
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()

    def write_to_file(file_name: str) -> None:
        with open(file_name, "w") as file:
            (file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"))
            line_counter = 1
            while True:
                line_input = input("Enter content line: ")
                if line_input == "stop":
                    return
                file.write(f"line {line_counter}: {line_input}")
                line_counter += 1

    path = os.path.join(*args.d)
    if args.d and not args.f:
        os.makedirs(path, exist_ok=True)
    elif args.f and not args.d:
        write_to_file(args.f)
    elif args.d and args.f:
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, args.f)
        write_to_file(file_path)
