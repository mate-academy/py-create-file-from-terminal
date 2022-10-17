import datetime
import os
import sys


def create_file() -> None:
    """
    Create sub folders and file
    Typically command line:
    "python create_file.py -d subdir1 subdir1 -f file.txt"
    """
    program_argv = sys.argv
    path_traverse = ""
    if "-d" in program_argv:
        folders = []
        index_found = program_argv.index("-d")
        for index in range(index_found + 1, len(program_argv)):
            if program_argv[index] != "-f":
                folders.append(program_argv[index])
            else:
                break

        if folders:
            for path in folders:
                path_traverse = os.path.join(path_traverse, path)
                if not os.path.isdir(path_traverse):
                    os.mkdir(path_traverse)

    file_name = ""
    if "-f" in program_argv:
        index_found = program_argv.index("-f")
        if index_found + 1 < len(program_argv):
            file_name = os.path.join(
                path_traverse, program_argv[index_found + 1])

    if file_name:
        open_param = "wt"
        if os.path.isfile(file_name):
            open_param = "at"

        lines = []
        is_continue = True
        while is_continue:
            new_line = input("Enter content line: ")
            if new_line.lower() != "stop":
                lines.append(new_line)
            else:
                is_continue = False

        with open(file_name, open_param) as file_obj:
            file_obj.write(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            for line in lines:
                file_obj.write(line + "\n")


if __name__ == "__main__":
    create_file()
