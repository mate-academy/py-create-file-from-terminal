from argparse import ArgumentParser, Namespace
import datetime
import os


def parse_arguments() -> Namespace:
    argparser = ArgumentParser(
        description="Create file from terminal"
    )
    argparser.add_argument(
        "-d",
        nargs="*",
        default="",
        help="Provide directory"
    )
    argparser.add_argument(
        "-f",
        type=str,
        default=False,
        help="Provide filename"
    )
    return argparser.parse_args()


def create_file(filename: str) -> None:
    timestamp = datetime.datetime.now()
    text = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
    line_number = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        text += f"{line_number} {content}\n"
        line_number += 1
    if os.path.exists(filename):
        with open(filename, "a") as f:
            text = "\n" + text
            f.write(text)
    else:
        with open(filename, "w") as f:
            f.write(text)


if __name__ == "__main__":
    args = parse_arguments()
    if args.d and not os.path.exists(os.path.join(*args.d)):
        os.makedirs(os.path.join(*args.d))
    if args.f:
        create_file(os.path.join(*args.d, args.f))
