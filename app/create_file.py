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
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        if text:
            for i, line in enumerate(text, start=1):
                file.write(f"{i} {line}\n")
            file.write("\n")


def text_input_from_user() -> list[str]:
    text_input = []

    while True:
        input_data = input("Enter content line: ")
        if input_data == "stop":
            break
        text_input.append(input_data)

    return text_input


def main() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        dir_index = sys.argv.index("-d")
        if dir_index + 1 >= len(sys.argv):
            raise ValueError("Directory path empty")
        create_directory(sys.argv[dir_index + 1:])
    elif "-f" in sys.argv and "-d" not in sys.argv:
        file_index = sys.argv.index("-f")
        if file_index + 1 >= len(sys.argv):
            raise ValueError("File name empty")
        file_path = sys.argv[file_index + 1]
        text_data = text_input_from_user()
        create_file(file_path, text_data)
    else:
        dir_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")

        # Validate file name existence
        if file_index + 1 >= len(sys.argv):
            raise ValueError("File name empty")

        # Validate directory path existence
        if dir_index + 1 >= len(sys.argv):
            raise ValueError("Directory path empty")

        if dir_index < file_index:
            in_dir_path = sys.argv[dir_index + 1:file_index]
            if not in_dir_path:
                raise ValueError("Directory path empty")
            out_dir_path = create_directory(in_dir_path)
            file_name = sys.argv[file_index + 1]
            file_path = os.path.join(out_dir_path, file_name)
            text_data = text_input_from_user()
            create_file(file_path, text_data)
        elif file_index < dir_index:
            file_name = sys.argv[file_index + 1]
            in_dir_path = sys.argv[dir_index + 1:]
            if not in_dir_path:
                raise ValueError("Directory path empty")
            out_dir_path = create_directory(in_dir_path)
            file_path = os.path.join(out_dir_path, file_name)
            text_data = text_input_from_user()
            create_file(file_path, text_data)


if __name__ == "__main__":
    main()
