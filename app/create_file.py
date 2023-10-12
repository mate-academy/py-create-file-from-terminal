import os
import sys
from datetime import datetime


def create_dir(dir_name: list) -> str:
    dir_path = os.path.join(*dir_name)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(file_name: str, path: str = os.getcwd()) -> None:
    with open(os.path.join(path, file_name), "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        line_num = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line.lower() == "stop":
                break
            f.write(f"{line_num} {new_line} \n")
            line_num += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = create_dir(
            sys.argv[
                sys.argv.index("-d") + 1:sys.argv.index("-f")
            ]
        )
        file_name = sys.argv[sys.argv.index("-f") + 1]
        create_file(file_name, path)
    elif "-d" in sys.argv:
        create_dir(sys.argv[sys.argv.index("-d") + 1:])

    elif "-f" in sys.argv:
        create_file(sys.argv[sys.argv.index("-f") + 1])


if __name__ == "__main__":
    main()
