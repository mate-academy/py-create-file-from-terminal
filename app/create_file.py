import os
import sys
from datetime import datetime

D_FLAG = "-d"
F_FLAG = "-f"


def create_file(command: list) -> None:
    dirs_to_create = get_string_after_flag(D_FLAG, command)
    file_name = get_string_after_flag(F_FLAG, command)

    process_flag(dirs_to_create, D_FLAG)

    if dirs_to_create and file_name:
        file_name = dirs_to_create + os.sep + file_name

    process_flag(file_name, F_FLAG)


def get_string_after_flag(flag: str, command: list) -> str:
    if flag in command:
        return command[command.index(flag) + 1]


def process_flag(path_or_file_name: str, flag: str) -> None:
    if path_or_file_name:
        path = os.path.normpath(os.getcwd() + os.sep + path_or_file_name)

        if not os.path.exists(path):
            if flag == D_FLAG:
                os.makedirs(path)
            if flag == F_FLAG:
                write_to_file(path, False)
            return

        if flag == F_FLAG:
            write_to_file(path, True)


def write_to_file(path: str, non_empty: bool) -> None:
    all_lines = ""
    line_counter = 1

    with (open(path, "a+") as file):
        while True:
            input_line = input(
                'Enter content line or "stop" to break input: '
            )
            if input_line == "stop":
                break
            all_lines += f"{line_counter} {input_line}\n"
            line_counter += 1

        if all_lines:
            all_lines = (
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                f"\n{all_lines}"
            )
            if non_empty:
                all_lines = "\n" + all_lines

            file.write(all_lines)


if __name__ == "__main__":
    create_file(sys.argv)
