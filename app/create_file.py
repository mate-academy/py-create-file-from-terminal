import os
import sys
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        line_number = 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1

def main():
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        directory_path = os.path.join(*sys.argv[dir_index + 1:])

        try:
            os.makedirs(directory_path)
        except FileExistsError:
            pass

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        file_name = sys.argv[file_index + 1]

        if "-d" in sys.argv:
            directory_path = os.path.join(*sys.argv[dir_index + 1:-3])
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        if os.path.exists(file_path):
            create_file(file_path)
        else:
            with open(file_path, "w") as file:
                line_number = 1
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}\n")
                while True:
                    line = input("Enter content line: ")
                    if line.lower() == "stop":
                        break
                    file.write(f"{line_number} {line}\n")
                    line_number += 1


if __name__ == "__main__":
    main()
