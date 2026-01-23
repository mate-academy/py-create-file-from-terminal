import os
import sys
import datetime


def create_path(args: list) -> str:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        directories = args[d_index + 1: f_index]
    else:
        directories = args[d_index + 1:]
    path = os.path.join(*directories)
    return path


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(args: list) -> None:
    path = args[-1]
    if "-d" in args:
        path = os.path.join(create_path(args), args[-1])

    with open(path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1

        while True:
            content = input("Enter content line:")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1

    return


def main() -> None:
    args = sys.argv

    if "-d" in args and "-f" not in args:
        create_directory(create_path(args))

    elif "-f" in args and "-d" not in args:
        create_file(args)

    elif "-d" in args and "-f" in args:
        create_directory(create_path(args))
        create_file(args)
    return


if __name__ == "__main__":
    main()
