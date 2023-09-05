import sys
import os
from datetime import datetime


def create_path(dirr: list) -> str:
    current_dir = os.getcwd()
    path = os.path.join(current_dir, *dirr)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d $H:%M:%S')} \n")
        number_line = 1
        while True:
            data = input("Enter content line: ")
            if data == "stop":
                file.write("\n")
                break
            file.write(f"{number_line} {data} \n")
            number_line += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        _, d_command, f_command, *dirr, file_name = sys.argv
        path = create_path(dirr)
        create_file(f"{path}/{file_name}")
        return
    if "-d" in sys.argv:
        _, d_command, *dirr = sys.argv
        create_path(dirr)
        return
    if "-f" in sys.argv:
        create_file(sys.argv[-1])
        return


if __name__ == "__main__":
    main()
