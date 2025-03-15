import os
import sys
import datetime


def create_file(file_path: str) -> None:

    with open(file_path, "a") as f:

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1


def create_directory(path: str) -> None:

    os.makedirs(path, exist_ok=True)


def main() -> None:

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d") + 1
        dir_path = os.path.join(*sys.argv[d_index:])
        create_directory(dir_path)

        if "-f" in sys.argv:
            f_index = sys.argv.index("-f") + 1
            file_name = sys.argv[f_index]
            full_file_path = os.path.join(dir_path, file_name)
            create_file(full_file_path)
    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f") + 1
        file_name = sys.argv[f_index]
        create_file(file_name)


if __name__ == "__main__":
    main()
