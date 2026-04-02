import os
import argparse

from datetime import datetime

from termcolor import colored
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="Create file and directory",
    description="Program create file and directories"
)

dir_arg = parser.add_argument(
    "-d",
    dest="dir",
    metavar="N",
    type=str,
    nargs="*",
    help="Create directory, example: -d dir1 dir2"
)
filename_arg = parser.add_argument(
    "-f",
    dest="filename",
    type=str,
    nargs="?",
    help="Create file, by filename, example: -f filename.txt"
)


def main() -> None:
    try:
        args = parser.parse_args()
        dirname = Path(__file__).resolve().parent

        if args.dir is None and args.filename is None:
            raise argparse.ArgumentError(
                None,
                (
                    "Use one of parameters: -d or -f. "
                    "Or use help for more details."
                )
            )

        if args.dir is not None:
            for new_dir in args.dir:
                dirname = os.path.join(dirname, new_dir)
                try:
                    os.makedirs(dirname)
                    print(
                        colored(
                            f"Directory '{new_dir}' successfully created.",
                            "green"
                        )
                    )
                except FileExistsError:
                    print(
                        colored(
                            f"Directory '{new_dir}' already exists.",
                            "yellow"
                        )
                    )
                    continue

        if args.filename is not None:
            path = os.path.join(dirname, args.filename)
            try:
                with open(path, "r") as new_file:
                    old_text = new_file.read()
            except FileNotFoundError:
                old_text = ""

            with open(path, "a") as new_file:
                lines = []
                if old_text:
                    lines.append("\n")
                now = datetime.now()
                text = now.strftime("%Y-%m-%d %H:%M:%S")
                while not text == "stop":
                    lines.append(text + "\n")
                    text = input("Enter content line: ")

                new_file.writelines(lines)
                print(
                    colored(
                        f"File '{args.filename}' successfully created.",
                        "green"
                    )
                )

    except argparse.ArgumentError as e:
        print(colored(e.message, "red"))


if __name__ == "__main__":
    main()
