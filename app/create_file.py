import os
import sys
from datetime import datetime


def usage() -> None:
    print(
        "Usage:\n"
        "  python create_file.py -f <filename>\n"
        "  python create_file.py -d <dir1> [<dir2> ...]\n"
        "  python create_file.py -d <dir1> [<dir2> ...] -f <filename>\n"
    )


def create_file(path: str) -> None:
    with open(path, "a", encoding="utf-8") as file:
        if file.tell() > 0:
            file.write("\n")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{ts}\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{counter} {text}\n")
            counter += 1


def main(args: list[str]) -> None:
    if len(args) < 2:
        print("Error: No flags provided (-d or -f).")
        usage()
        sys.exit(1)

    has_d = "-d" in args
    has_f = "-f" in args

    if not has_d and not has_f:
        print("Error: Unknown flag. Use -d or -f.")
        usage()
        sys.exit(1)

    if has_d and has_f:
        d_idx = args.index("-d")
        f_idx = args.index("-f")
        if d_idx < f_idx:
            dirs = args[d_idx + 1 : f_idx]
        else:
            dirs = args[d_idx + 1 :]

        if not dirs:
            print("Error: No directories provided after -d.")
            sys.exit(1)

        if f_idx + 1 >= len(args):
            print("Error: Filename is missing after -f.")
            sys.exit(1)

        filename = args[f_idx + 1]
        dir_path = os.path.join(os.getcwd(), *dirs)
        os.makedirs(dir_path, exist_ok=True)
        create_file(os.path.join(dir_path, filename))
        return

    if has_d:
        d_idx = args.index("-d")
        dirs = args[d_idx + 1 :]
        if not dirs:
            print("Error: No directories provided after -d.")
            sys.exit(1)
        dir_path = os.path.join(os.getcwd(), *dirs)
        os.makedirs(dir_path, exist_ok=True)
        return

    if has_f:
        f_idx = args.index("-f")
        if f_idx + 1 >= len(args):
            print("Error: Filename is missing after -f.")
            sys.exit(1)
        filename = args[f_idx + 1]
        create_file(os.path.join(os.getcwd(), filename))
        return


if __name__ == "__main__":
    main(sys.argv)
