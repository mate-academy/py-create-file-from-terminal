import os
import argparse
from datetime import datetime


def main(dir_path: list[str] = None, file_name: str = None) -> None:
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
    if os.path.exists(file_path):
        with open(file_path) as file:
            count = len(file.readlines()) - 1

    utc_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        count += 1
        text = input("Enter content line: ")
        if text.lower() == "stop":
            break
        if not os.path.exists(file_path):
            with open(file_path, "w") as file_time:
                file_time.write(utc_time + "\n")
                file_time.write(f"{count} {text} \n")
        else:
            with open(file_path, "a") as file:
                file.write(f"{count} {text} \n")


parser = argparse.ArgumentParser(description="Create file with input")

parser.add_argument("-d", nargs="+", dest="dir_path")
parser.add_argument("-f", dest="file_name")

args = parser.parse_args()

if __name__ == "__main__":
    main(args.dir_path, args.file_name)
