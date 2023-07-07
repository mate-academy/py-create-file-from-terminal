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

    if "-d" == input_list[1]:
        parent_dir = os.getcwd()
        for directory in input_list[2:]:
            if directory == "-f":
                file_path = os.path.join(parent_dir, input_list[-1])
                create_file_func(file_path)
                break
            new_dir = os.path.join(parent_dir, directory)
            os.makedirs(new_dir, exist_ok=True)
            parent_dir = new_dir

    if "-f" == input_list[1]:
        if len(input_list) > 3:
            path = os.path.join(os.getcwd(), *input_list[4:])
            os.makedirs(path, exist_ok=True)
            file_path = os.path.join(path, input_list[2])
            create_file_func(file_path)
        else:
            create_file_func(input_list[2])


if __name__ == "__main__":
    create_file()
