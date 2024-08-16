import os
import sys
import argparse
from datetime import datetime


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("-d", nargs=argparse.ZERO_OR_MORE)
argument_parser.add_argument("-f", nargs=argparse.OPTIONAL)


def main(args: list[str]) -> None:
    args = argument_parser.parse_args(args)

    if args.d:
        full_path = os.path.join(*args.d)
        os.makedirs(full_path, exist_ok=True)
    else:
        full_path = ""

    if not args.f:
        return

    full_path = os.path.join(full_path, args.f)
    add_extra_newline = os.path.isfile(full_path)
    with open(full_path, "a") as file:
        if add_extra_newline:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_counter = 1
        while (line := input("Enter content line: ")) != "stop":
            file.write(f"{line_counter} {line}\n")
            line_counter += 1
        file.write("\n")


if __name__ == "__main__":
    main(sys.argv[1:])
