import argparse
import os
from datetime import datetime


def parse_args() -> type[str, str]:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--dir", nargs="+", default=".")
    parser.add_argument("-f", "--file_name", default="file.txt")

    args = parser.parse_args()

    path_to_dir = os.path.join(*args.dir)
    return path_to_dir, os.path.join(path_to_dir, args.file_name)


def check_and_create_new_path(path_to_dir: str, file_path: str) -> None:
    if not os.path.exists(path_to_dir):
        os.makedirs(path_to_dir)

    if not os.path.exists(file_path):
        open(file_path, "w")


def main() -> None:
    path_to_dir, file_path = parse_args()
    check_and_create_new_path(path_to_dir, file_path)

    with open(file_path, "a") as f:
        f.writelines(
            datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + "\n"
        )

        count = 1
        while True:
            users_input = input("Enter content line: ")
            if users_input == "stop":
                f.write("\n")
                break
            count += 1
            f.write(f"{count} {users_input}\n")


if __name__ == "__main__":
    main()
