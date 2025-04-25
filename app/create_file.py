import os

from datetime import datetime

from itertools import count

import os.path


def create_file() -> None:
    first_str = input("Enter path and name: ")
    first_list = first_str.split(" ")
    if "-d" in first_str:
        d_index = first_list.index("-d")
        path_list = first_list[(d_index + 1):]
        path_dir = "".join(path_list)
        os.makedirs(path_dir, exist_ok=True)
    if "-f" in first_str:
        f_index = first_list.index("-f")
        file_name = first_list[f_index + 1]
        with open(file_name, "a") as file:
            now = datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_time}\n")
            infinite_iterator = count(1)
            for i in infinite_iterator:
                file_content = input("Enter content line: ")
                if file_content == "stop":
                    file.write("\n")
                    break
                file.write(f"{i} {file_content}\n")
        os.path.join("path_dir", file_name)


if __name__ == "__main__":
    create_file()
