import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv
    directory_path = ""
    if "-d" in args:
        d_index = args.index("-d")
        stop_index = args.index("-f") if "-f" in args else len(args)
        dir_names = args[d_index + 1 : stop_index]
        directory_path = os.path.join(*dir_names)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        full_path = os.path.join(directory_path, file_name)
        if directory_path.strip():
            os.makedirs(directory_path, exist_ok=True)

        with open(full_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp)

            line_number = 1
            while True:
                content = input("Enter content line: ")

                if content == "stop":
                    file.write("\n")
                    break

                file.write(f"{line_number} {content}")
                line_number += 1


if __name__ == "__main__":
    create_file()
