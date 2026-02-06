import os
import sys
from datetime import datetime


def create_directory(directory: list[str]) -> str:
    path_for_file = ""
    full_path = os.getcwd()
    for folder in directory:
        full_path = os.path.join(full_path, folder)

        if os.path.exists(full_path) and os.path.isfile(full_path):
            raise NotADirectoryError(full_path)

        os.makedirs(full_path, exist_ok=True)
        path_for_file = full_path

    return path_for_file


def create_file(file_name: str, text: list[str]) -> None:
    if not file_name:
        raise FileNotFoundError

    with open(file_name, "a") as file:
        file.writelines(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "\n")
        if text:
            for line in text:
                file.write(line + "\n")
            file.write("\n")


def main() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        dir_index = sys.argv.index("-d")
        create_directory(sys.argv[dir_index + 1:])
    elif "-f" in sys.argv and "-d" not in sys.argv:
        file_index = sys.argv.index("-f")
        file_path = sys.argv[file_index + 1]
        text_input = []
        while True:
            input_data = input("Enter content line: ")
            if input_data != "stop":
                text_input.append(input_data)
            else:
                break
        create_file(file_path, text_input)
    else:
        dir_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")
        in_dir_path = sys.argv[dir_index + 1:file_index]
        out_dir_path = create_directory(in_dir_path)
        text_input = []
        file_name = sys.argv[file_index + 1]
        file_path = os.path.join(out_dir_path, file_name)
        while True:
            input_data = input("Enter content line: ")
            if input_data != "stop":
                text_input.append(input_data)
            else:
                break
        create_file(file_path, text_input)


if __name__ == "__main__":
    main()
