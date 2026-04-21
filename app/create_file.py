import os
from datetime import datetime
import sys


def main() -> None:
    filename = ""
    write_dir = os.getcwd()
    args = sys.argv

    # extract filename to create from arg
    try:
        file_index = args.index("-f")
        filename = args[file_index + 1]
    except (ValueError, IndexError):
        raise ValueError("Program requires mandatory file flag -f <filename>")

    # extract optional directories to create from arg
    try:
        dir_index = args.index("-d")
        if file_index < dir_index:
            directories_to_create = " ".join(args[dir_index + 1:])
        else:
            directories_to_create = " ".join(args[dir_index + 1:file_index:1])

        # no directory name provided with -d flag
        if directories_to_create == "":
            raise IndexError

        # create absolute directory path
        for directory in directories_to_create.split():
            write_dir = os.path.join(write_dir, directory)

    except ValueError:
        # no directory flag provided - ignore
        pass
    except IndexError:
        raise ValueError(
            "Program requires directories to create with flag "
            "-d <dir1> <dir2> ... <dirX>"
        )

    # check if director exists and create otherwise
    if not os.path.exists(write_dir):
        os.makedirs(write_dir)

    # create file from input text
    output_file = open(f"{os.path.join(write_dir, filename)}", "a")
    output_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    line_no = 1
    while True:
        entered_text = input("Enter content line: ")

        if entered_text == "stop":
            output_file.write("\n")
            break

        output_file.write(f"{line_no} {entered_text}" + "\n")
        line_no += 1

    output_file.close()


if __name__ == "__main__":
    main()
