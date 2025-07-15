import sys
import os
from datetime import datetime


def file_writer(name: str) -> None:
    with open(name, "a") as file_open:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_open.write(current_time + "\n")
        line = 1

        while True:
            content = input("Enter content line: ")

            if content.lower() == "stop":
                break
            file_open.write(f"{line} {content}\n")
            line += 1

        file_open.write("\n")


def create_file(args: list) -> None:
    f_index = args.index("-f")

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        dir_path = args[d_index + 1 : f_index]
        file_name = args[f_index + 1]

    elif "-d" in args:
        d_index = args.index("-d")
        dir_path = args[d_index + 1 : f_index]
        file_name = None

    elif "-f" in args:
        dir_path = []
        file_name = args[f_index + 1]

    else:
        print("Error: No flags provided")
        return

    if dir_path:
        dir_path = os.path.join(*dir_path)
        os.makedirs(dir_path, exist_ok=True)
    dir_path = "."

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        file_writer(file_path)


if __name__ == "__main__":
    create_file(sys.argv[1:])
