import os
import sys
from datetime import datetime


def main() -> None:
    arg_list = sys.argv[1:]
    file_name = ""
    current_path = ""

    if "-f" in sys.argv:
        file_name = arg_list.pop(arg_list.index("-f") + 1)
        arg_list.remove("-f")

    if "-d" in sys.argv:
        arg_list.remove("-d")
        current_path = os.path.join(*arg_list)
        if not os.path.exists(current_path):
            os.makedirs(current_path)

    if file_name:
        create_file(str(os.path.join(current_path, file_name)))


def create_file(file_name: str) -> None:
    with open(file_name, "a") as update_file:
        update_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_num = 1
        while True:
            info = input("Enter content line:")
            if info == "stop":
                update_file.write("\n")
                break
            update_file.write(f"{line_num} {info}\n")
            line_num += 1


if __name__ == "__main__":
    main()
