# write your code here
import sys
import os.path
from datetime import datetime


def write_to_file(file_path: str) -> None:
    with open(file_path, "a") as source_file:
        source_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        count = 1
        while True:
            text_input = input("Enter content line: ")
            if text_input == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{count} {text_input}\n")
            count += 1


def read_terminal_args() -> str | None:
    _, *arguments = sys.argv
    is_f_flag_exists = False
    try:
        idx_filename = arguments.index("-f") + 1
        is_f_flag_exists = True
    except ValueError:
        filename = "file.txt"
    else:
        filename = arguments[idx_filename]

    try:
        idx_start = arguments.index("-d") + 1
    except ValueError:
        folders = []
    else:
        try:
            idx_end = arguments.index("-f")
        except ValueError:
            idx_end = len(arguments)
        finally:
            folders = arguments[idx_start:idx_end]
    if not is_f_flag_exists:
        if not os.path.exists(os.path.join(*folders)):
            os.makedirs(os.path.join(*folders))
        return
    return write_to_file(os.path.join(*folders, filename))


if __name__ == "__main__":
    read_terminal_args()
