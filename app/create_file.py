import os
import argparse
from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser(description="Create file with input")

    parser.add_argument("-d", nargs="+", dest="dir_path")
    parser.add_argument("-f", dest="file_name")

    args = parser.parse_args()
    dir_path = args.dir_path
    file_name = args.file_name

    if dir_path:
        path = os.path.join(*dir_path)
        os.makedirs(path, exist_ok=True)
    if file_name:
        if dir_path:
            file_path = os.path.join(*dir_path, file_name)
            data_input(file_path)
        else:
            data_input(file_name)


def data_input(file_path: str) -> None:
    count = 0
    utc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file_time:
        file_time.write(f"{utc_time}\n")

        while True:
            count += 1
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file_time.write(f"{count} {text}\n")

        file_time.write("\n")


if __name__ == "__main__":
    main()
