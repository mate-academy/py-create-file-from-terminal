import os
import sys
from datetime import datetime


def create_file(path_file: str) -> None:
    with open(path_file, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            user_line = input("Enter content line: ")
            if user_line == "stop":
                file.write("\n")
                break
            file.write(user_line + "\n")


def main() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        d_index = sys.argv.index("-d")
        directory_name = os.path.join(*sys.argv[d_index + 1:])

        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

    elif "-f" in sys.argv and "-d" not in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[-1]
        create_file(file_name)

    elif "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        directory_name = os.path.join(*sys.argv[d_index + 1:f_index])
        file_name = sys.argv[-1]

        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        create_file(os.path.join(directory_name, file_name))


if __name__ == "__main__":
    main()
