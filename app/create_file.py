import sys
import os
from datetime import datetime


def how_to_use() -> None:
    print("""
Create file from the terminal.
Format:
    py create_file.py -d dir1 [ .. dirN] [-f filename.ext]
        or
    py create_file.py -f filename.ext [-d dir1 [ .. dirN]]

Enter line by line to file from the terminal. To complete - enter "stop" """)


def parse_cmd(list_args: list) -> None:
    # output:  fpath = {"dirs": "", "filename": ""}
    fpath = {}

    idx_f = len(list_args)
    if "-f" in list_args:
        idx_f = list_args.index("-f")
        fpath["filename"] = "".join(list_args[idx_f + 1:idx_f + 2])

    if "-d" in list_args:
        idx_d = list_args.index("-d")
        fpath["dirs"] = os.path.join(
            *list_args[idx_d + 1: idx_f] if idx_d < idx_f
            else list_args[idx_d + 1:]
            , "")
    return fpath


def create_dirs(path_dirs: str) -> None:
    try:
        os.makedirs(path_dirs, exist_ok=True)
    except OSError as e:
        print("OSError: Directory name Syntax Error")
        print(e)
        sys.exit(123)


def write_input_to_file(full_path: str) -> None:
    try:
        with open(full_path, "a+") as f:
            f.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
            number = 1
            while True:
                inp_str = input("Enter content line: ")
                if inp_str.lower() == "stop":
                    break
                f.write(f"{str(number)} {inp_str}\n")
                number += 1
            f.write("\n")
    except OSError as e:
        print("OSError: File I/O Error")
        print(e)
        sys.exit(22)


def main() -> None:
    # py create_file.py -d dir1 dir2 .. dirN -f filename.ext

    fpath = parse_cmd(sys.argv[1:])

    if fpath:
        full_path = os.path.join(
            os.getcwd(),
            fpath.get("dirs", ""),
            fpath.get("filename", ""))

        if fpath.get("dirs", None):
            create_dirs(fpath["dirs"])

        if fpath.get("filename", None):
            write_input_to_file(full_path)
    else:
        how_to_use()


if __name__ == "__main__":
    main()
