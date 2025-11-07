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


def main(args: list) -> None:
    if len(args) < 2:
        print("Error: No flags provided (-d or -f).")
        usage()
        sys.exit(1)

    flag = args[1]

    if flag == "-d":
        if "-f" in args:
            f_idx = args.index("-f")
            dirs = args[2:f_idx]
            if f_idx + 1 >= len(args):
                print("Error: Filename is missing after -f.")
                sys.exit(1)
            filename = args[f_idx + 1]
        else:
            dirs = args[2:]
            filename = None

        if not dirs:
            print("Error: No directories provided after -d.")
            sys.exit(1)

        dir_path = os.path.join(os.getcwd(), *dirs)
        os.makedirs(dir_path, exist_ok=True)

        if filename is not None:
            path = os.path.join(dir_path, filename)
            create_file(path)

    elif flag == "-f":
        if len(args) < 3:
            print("Error: Filename is missing after -f.")
            sys.exit(1)
        filename = args[2]
        path = os.path.join(os.getcwd(), filename)
        create_file(path)

    else:
        print("Error: Unknown flag. Use -d or -f.")
        usage()
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
