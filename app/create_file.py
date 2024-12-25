import sys
import os
from datetime import datetime


def create_directory_and_file() -> None:
    path = os.getcwd()
    if "-d" in sys.argv:
        index_d_command = sys.argv.index("-d")
        if (
            (index_d_command + 1) < len(sys.argv)
            and not sys.argv[index_d_command + 1].startswith("-")
        ):
            directory = sys.argv[index_d_command + 1]
            path = os.path.abspath(directory)
            os.makedirs(path, exist_ok=True)

    if "-f" in sys.argv:
        index_f_command = sys.argv.index("-f")
        file_name = sys.argv[index_f_command + 1]
        file_path = os.path.join(path, file_name)
        with open(file_path, "a") as f:
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            f.write(f"{timestamp}\n")
            line_number = 1
            while True:
                content = input(f"enter content line {line_number}: ")
                if content.lower() == "stop":
                    break
                f.write(f"{line_number} {content}\n")
                line_number += 1


if __name__ == "__main__":
    create_directory_and_file()
