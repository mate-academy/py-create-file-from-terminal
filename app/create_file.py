import os
import argparse
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dirs")
    parser.add_argument("-f", dest="file")
    path = ""

    if parser.parse_args().dirs:
        path = os.path.join(path, parser.parse_args().dirs)
        os.makedirs(path, exist_ok=True)
    if parser.parse_args().file:
        path = os.path.join(path, parser.parse_args().file)
        with open(path, "a") as f:
            f.write(str(datetime.now()))
            line_index = 1
            while True:
                text = input("Enter content line: ")
                if text.lower() == "stop":
                    break
                f.write(f"{line_index}: {text}\n")
                line_index += 1


if __name__ == "__main__":
    create_file()
