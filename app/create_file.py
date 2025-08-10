import argparse
import os
import time


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dirs", nargs="*", help="Create dictionary")
    parser.add_argument("-f", dest="file", help="Crate files")
    args = parser.parse_args()
    path = ""

    if args.dirs:
        path = os.path.join(path, *args.dirs)
        os.makedirs(path, exist_ok=True)

    if args.file:
        path = os.path.join(path, args.file)
        with open(path, "a") as file:
            file.write(time.strftime("\n%Y-%m-%d, %H:%M:%S\n"))
            number = 1
            while True:
                text_user = input("Enter content line: ")
                if text_user.lower() == "stop":
                    break
                file.writelines(f"{number} {text_user}\n")
                number += 1


if __name__ == "__main__":
    create_file()
