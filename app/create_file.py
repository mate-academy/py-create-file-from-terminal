import sys
import os
from datetime import datetime
from typing import LiteralString


def create_file_in_terminal(path_of_file: str) -> None:
    with open(path_of_file, "a") as file:
        now = datetime.now()  # поточний час і дата
        file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while True:
            str_for_write = input("Enter content line:")
            if str_for_write.lower() != "stop":
                file.writelines(f"{line_number} {str_for_write}\n")
            else:
                file.writelines("\n")
                break


def create_dir_in_terminal(
        path_of_dir: LiteralString | bytes | str
) -> None:
    os.makedirs(path_of_dir, exist_ok=True)


def create_file_from_terminal() -> None:
    current_params = sys.argv
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")

        # Аргументи між -d і -f → це директорії
        folders = sys.argv[d_index : f_index - 1]
        dir_path = os.path.join(*folders)
        create_dir_in_terminal(dir_path)

        file_name = sys.argv[f_index]
        file_path = os.path.join(dir_path, file_name)
        create_file_in_terminal(file_path)

    if "-f" == current_params[1]:
        create_file_in_terminal(current_params[2])

    if "-d" == current_params[1]:
        create_dir_in_terminal(os.path.join(
            *current_params[2:-1], current_params[-1])
        )


if __name__ == "__main__":
    create_file_from_terminal()
