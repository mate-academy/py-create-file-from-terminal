import sys
import os
from datetime import datetime


def is_valid_cli_command(command: list[str]) -> bool:
    if "-f" not in command:
        return False

    return True


def get_input_lines_values() -> str:
    is_stopped = False
    line_number = 1
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = f"{date}\n"

    while not is_stopped:
        input_value = input("Enter the value: ")

        if input_value == "stop":
            is_stopped = True
            break

        lines += f"{line_number} {input_value}\n"
        line_number += 1

    return lines


def get_created_dirs_path(root_path: str, terminal_args: list[str]) -> str:
    file_command_index = terminal_args.index("-f")
    dirs_names = terminal_args[1:file_command_index]
    os.makedirs("/".join(dirs_names), exist_ok=True)
    return os.path.join(root_path, *dirs_names)


def generate_file(path: str, file_name: str, content: str) -> None:
    with open(os.path.join(path, file_name), "w", encoding="utf-8") as file:
        file.write(content)


def create_file_cli(terminal_args: list[str]) -> None:
    if not is_valid_cli_command(terminal_args):
        return

    path = os.getcwd()
    file_name = terminal_args[-1]

    if "-d" in terminal_args:
        path = get_created_dirs_path(path, terminal_args[1:])

    content = get_input_lines_values()
    generate_file(path, file_name, content)


if __name__ == "__main__":
    create_file_cli(sys.argv)
