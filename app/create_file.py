import os
from datetime import datetime
import sys


def parse_args() -> tuple:
    # extract filename to create from args
    write_dir = os.getcwd()
    args = sys.argv
    try:
        file_index = args.index("-f")
        filename = args[file_index + 1]
    except ValueError:
        file_index = 0
        filename = ""
    except IndexError:
        raise ValueError(
            "Program requires mandatory file name "
            "with flag -f <filename>"
        )

    # extract optional directories to create from arg
    try:
        if "-d" in args:
            dir_index = args.index("-d")
            if file_index < dir_index:
                directories_to_create = " ".join(args[dir_index + 1:])
            else:
                directories_to_create = (
                    " ".join(args[dir_index + 1:file_index:1])
                )

            # no directory name provided with -d flag
            if directories_to_create == "":
                raise ValueError(
                    "Program requires directories to create with flag "
                    "-d <dir1> <dir2> ... <dirX>"
                )

            # create absolute directory path
            for directory in directories_to_create.split():
                write_dir = os.path.join(write_dir, directory)

    except IndexError:
        raise ValueError(
            "Program requires directories to create with flag "
            "-d <dir1> <dir2> ... <dirX>"
        )
    return (write_dir, filename)


def write_file(write_dir: str, filename: str) -> None:
    # create file from input text
    output_file = open(f"{os.path.join(write_dir, filename)}", "a")

    with open(f"{os.path.join(write_dir, filename)}", "a") as output_file:
        line_no = 1
        while True:
            entered_text = input("Enter content line: ")

            if entered_text == "stop":
                if line_no > 1:
                    output_file.write("\n")
                break

            if line_no == 1:
                output_file.write(
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                )

            output_file.write(f"{line_no} {entered_text}" + "\n")
            line_no += 1


def main() -> None:
    # parse arguments
    write_dir, filename = parse_args()

    # check directories if required
    os.makedirs(write_dir, exist_ok=True)

    # write file if specified
    if filename != "":
        write_file(write_dir, filename)


if __name__ == "__main__":
    main()
