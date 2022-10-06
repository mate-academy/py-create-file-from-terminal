import os
import argparse
import datetime


def create_file_from_terminal(cmd_line: str) -> None:
    """create_file_from_terminal(cmd_line: str)

    Parse command line and create directories and file.
    Flags:
        -d - create directory with given names
        -f - create file with given name
    Content of the file should be entered by user from terminal.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir_name", nargs="+")
    parser.add_argument("-f", dest="file_name", nargs=1)
    args = parser.parse_args(cmd_line.split())

    file_path = os.path.curdir

    if args.dir_name:
        file_path = f"{os.sep}".join(args.dir_name)
        os.makedirs(file_path, 0o777, True)

    if args.file_name:
        file_name = os.path.join(file_path, args.file_name[0])
        line_number = 1

        with open(file_name, "a") as text_file:
            line_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            text_file.write(f"{line_date}\n")

            while True:
                line_content = input("Enter content line: ")

                if line_content == "stop":
                    text_file.write("\n")
                    break

                text_file.write(f"{line_number} {line_content}\n")
                line_number += 1
