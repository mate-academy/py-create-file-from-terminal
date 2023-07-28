import sys
import os
from datetime import datetime


def create_path(sys_args: list) -> tuple:
    directory_path = None
    file_path = None

    if "-f" in sys_args:
        file_name_index = sys_args.index("-f")
        file_path = sys_args.pop(file_name_index + 1)
        sys_args.remove("-f")

    directory_names = sys_args[2:]

    if directory_names:
        directory_path = os.path.join(*directory_names)
        directory_path = directory_path
        if file_path:
            file_path = os.path.join(
                directory_path, file_path
            )

    return directory_path, file_path


def create_file() -> None:
    directory_path, file_path = create_path(sys.argv)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_path:
        with open(file_path, "a") as source_file:
            source_file.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

            while True:
                user_input = input("Enter content line:")
                if user_input == "stop":
                    source_file.write("\n")
                    break
                source_file.write(f"{user_input}\n")


if __name__ == "__main__":
    create_file()
