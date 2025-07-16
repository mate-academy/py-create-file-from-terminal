import os
import datetime
import argparse
from typing import List


def create_patch(segments: List[str]) -> str:
    patch = os.path.join(*segments)
    return patch


def make_dir(patch_dir: str) -> None:
    os.makedirs(patch_dir, exist_ok=True)


parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="+")
parser.add_argument("-f")
args = parser.parse_args()


def create_and_write_file(file_patch: str) -> None:
    current_datetime = datetime.datetime.now()
    datetime_info = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_patch, "a") as f:
        f.write(f"{datetime_info}\n")
        line = 1

        while True:
            input_line = input("Please write you text...")
            if input_line == "stop":
                break
            f.write(f"{line}, {input_line}\n")
            line += 1
            f.write("\n")


def create_file() -> None:
    if args.d and args.f:
        make_dir(create_patch(args.d))
        patch_to_create_file = [*args.d, args.f]
        create_and_write_file(create_patch(patch_to_create_file))

    if args.d:
        dears_to_create = create_patch(args.d)
        make_dir(dears_to_create)

    if args.f:
        make_file = args.f
        create_and_write_file(os.path.abspath(make_file))


if __name__ == "__main__":
    create_file()
