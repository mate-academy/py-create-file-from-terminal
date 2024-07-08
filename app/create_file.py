import sys
import os
from datetime import datetime


def create_file(path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name)

    os.makedirs(path, exist_ok=True)

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_num = 1
        while True:
            content = input("Enter content line:")
            if content.lower() == "stop":
                break
            file.write(f"Line{line_num} {content}\n")
            line_num += 1


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py -d dir1 dir2 -f file.txt")
        return

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f") if "-f" in sys.argv else None

        if f_index:
            dir_path = os.path.join(*sys.argv[d_index + 1:f_index])
            filename = sys.argv[f_index + 1]
        else:
            dir_path = os.path.join(*sys.argv[d_index + 1:])
            filename = None

    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        dir_path = os.getcwd()
        filename = sys.argv[f_index + 1]\

    if filename:
        create_file(dir_path, filename)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory {dir_path} created.")


if __name__ == "__main__":
    main()
