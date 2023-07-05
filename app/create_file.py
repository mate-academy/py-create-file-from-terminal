from datetime import datetime as dt
import sys
import os


def create_file_func(path: str) -> None:
    data_time = f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    with open(path, "a") as txt_file:
        txt_file.write(data_time)
        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                txt_file.write("\n")
                break
            txt_file.write(f"{line} {content}\n")
            line += 1


def create_file() -> None:
    input_list = sys.argv
    if "-d" in input_list:
        parent_dir = os.getcwd()
        for directory in input_list[1:]:
            new_dir = os.path.join(parent_dir, directory)
            os.makedirs(new_dir)
            parent_dir = new_dir

    if "-f" in input_list:
        create_file_func(input_list[1])


if __name__ == "__main__":
    create_file()
