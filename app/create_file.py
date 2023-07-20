from datetime import datetime
import os
import sys


def create_file_from_terminal() -> None:
    cut_argv = sys.argv[1:]
    folder_marker = False
    path_to = ""

    if cut_argv[0] == "-d" and cut_argv[-2] == "-f":
        path_to = f"{'/'.join(cut_argv[1:len(cut_argv) - 2])}"
        folder_marker = True

    if cut_argv[0] == "-d" and cut_argv[-2] != "-f":
        path_to = f"{'/'.join(cut_argv[1:])}"
        folder_marker = True

    if cut_argv[0] == "-f" and len(cut_argv) > 2:
        path_to = f"{'/'.join(cut_argv[3:])}"
        folder_marker = True

    if folder_marker:
        if "/" in path_to:
            os.makedirs(path_to, exist_ok=True)
        else:
            os.mkdir(path_to)
        path_to = f"{path_to}/file.txt"

    if cut_argv[0] == "-f" and len(cut_argv) == 2:
        path_to = "file.txt"

    with open(path_to, "a") as input_info:
        timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        line_number = 1
        input_info.write(f"{timestamp}\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                input_info.write("\n")
                break
            input_info.write(f"{line_number} {content}\n")
            line_number += 1


if __name__ == "__main__":
    create_file_from_terminal()
