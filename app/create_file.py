# write your code here
import sys
import os.path
from datetime import datetime


def read_terminal_args() -> str:
    _, *arguments = sys.argv
    print(arguments)
    try:
        idx_filename = arguments.index("-f") + 1
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
    return os.path.join(*folders, filename)


def write_to_file(file_path: str) -> None:
    path_to_file = os.path.split(file_path)[0]
    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)
    with open(file_path, "a") as source_file:
        source_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        count = 1
        while text_input := input("Enter content line: "):
            if text_input == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{count} {text_input}\n")
            count += 1


if __name__ == "__main__":
    path_to_file = read_terminal_args()
    write_to_file(path_to_file)
