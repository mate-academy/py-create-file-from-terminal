import argparse
import os
import datetime


def write_in_file(file_name: str) -> None:
    with open(file_name, "a+") as file:
        line_number = 1

        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )

        while True:
            content = input("Enter content line: ")

            if content == "stop":
                break

            file.write(f"{line_number} {content}\n")
            line_number += 1
        file.write("\n")


def make_dirs(*path) -> None:
    dir_path = os.path.join(*path)

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", nargs="+", help="Directory path")
    parser.add_argument("-f", type=str, help="File name")

    args = parser.parse_args()

    if args.d and args.f:
        make_dirs(*args.d)

        write_in_file(os.path.join(*args.d, args.f))
    elif args.d:
        make_dirs(*args.d)
    elif args.f:
        write_in_file(args.f)
    else:
        print("Provide flag for script")
