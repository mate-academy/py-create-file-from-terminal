import os
import argparse
import datetime as dt


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        nargs="*",
        help=(
            "all items (exclude -f) after this "
            "flag are parts of the path"
        )
    )
    parser.add_argument(
        "-f",
        help="first item after this flag is the file name"
    )
    return parser.parse_args()


def write_in_file(path: str) -> None:
    data = ""
    if os.path.exists(path):
        data += "\n"
    with open(path, "a+") as file:
        data += f'{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
        count = 1
        while (line := input("Enter content line: ")) != "stop":
            data += f"{count} {line}\n"
            count += 1
        file.write(data)


def main() -> None:
    args = get_arguments()

    path = ""
    if args.d:
        path = os.path.join(*args.d)
        os.makedirs(path, exist_ok=True)

    if args.f:
        path = os.path.join(path, args.f)
        write_in_file(path)


if __name__ == "__main__":
    main()
