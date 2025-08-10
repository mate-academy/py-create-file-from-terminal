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
    # output:  file_path = {"dirs": "", "filename": ""}
    file_path = {}

    index_filename = len(list_args)
    if "-f" in list_args:
        index_filename = list_args.index("-f")
        file_path["filename"] = "".join(
            list_args[index_filename + 1:index_filename + 2]
        )

    if "-d" in list_args:
        index_dirs = list_args.index("-d")
        file_path["dirs"] = os.path.join(
            *list_args[index_dirs + 1: index_filename]
            if index_dirs < index_filename else list_args[index_dirs + 1:]
            , "")
    return file_path


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
            f.write(f"""{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n""")
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

    file_path = parse_cmd(sys.argv[1:])

    if file_path:
        full_path = os.path.join(
            os.getcwd(),
            file_path.get("dirs", ""),
            file_path.get("filename", ""))

        if file_path.get("dirs", None):
            create_dirs(file_path["dirs"])

        if file_path.get("filename", None):
            write_input_to_file(full_path)
    else:
        how_to_use()


if __name__ == "__main__":
    main()
