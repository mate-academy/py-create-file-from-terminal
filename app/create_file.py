from datetime import datetime
import os
import sys


def create_file_from_terminal() -> None:
    path_to = ""
    filename = "file.txt"

    if "-d" in sys.argv:
        if "-f" in sys.argv:
            if sys.argv.index("-d") > sys.argv.index("-f"):
                path_to = sys.argv[4:]
                filename = sys.argv[2]
            else:
                path_to = sys.argv[2:len(sys.argv) - 2]
                filename = sys.argv[-1]
        else:
            path_to = sys.argv[2:]
        os.makedirs(os.path.join(*path_to), exist_ok=True)

    if "-f" in sys.argv and "-d" not in sys.argv:
        filename = sys.argv[2]

    with open(os.path.join(*path_to, filename), "a") as input_info:
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
