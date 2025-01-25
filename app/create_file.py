import sys
from datetime import datetime
import os


def read_text_for_file() -> list:
    line_number = 1
    text_to_write = []

    while 1:
        input_text = input("Enter content line: ")
        if input_text == "stop":
            break

        text = f"{line_number} {input_text}\n"
        text_to_write.append(text)
        line_number += 1

    return text_to_write


def create_dirs() -> os.path:
    index_d_flag = sys.argv.index("-d")
    path_to_dirs = os.path.join(
        sys.argv[index_d_flag + 1], sys.argv[index_d_flag + 2]
    )
    os.makedirs(path_to_dirs)
    return path_to_dirs


def create_file(dir_path: os.path = "") -> None:
    file_name = sys.argv[sys.argv.index("-f") + 1]
    file_path = os.path.join(dir_path, file_name)

    content = read_text_for_file()

    with open(file_path, "a") as file_out:
        file_out.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file_out.writelines(content)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path_to_file = create_dirs()
        create_file(path_to_file)
    elif "-d" in sys.argv:
        create_dirs()
    elif "-f" in sys.argv:
        create_file()


if __name__ == "__main__":
    main()
