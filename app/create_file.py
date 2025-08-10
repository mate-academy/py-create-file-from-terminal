import os
import sys
from datetime import datetime


def process_terminal_input(terminal_input: list) -> str | None:
    if "-d" in terminal_input and "-f" in terminal_input:
        index_d = terminal_input.index("-d")
        index_f = terminal_input.index("-f")
        dir_path = os.path.join(*terminal_input[(index_d + 1):index_f])
        os.makedirs(dir_path, exist_ok=True)
        file_name = terminal_input[index_f + 1]
        return os.path.join(dir_path, file_name)

    if "-d" in terminal_input:
        index = terminal_input.index("-d")
        dir_path = os.path.join(*terminal_input[(index + 1):])
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in terminal_input:
        index = terminal_input.index("-f")
        file_name = terminal_input[index + 1]
        return file_name


def create_file_or_write_into_it(file_path: str) -> None:
    with open(f"{file_path}", "a") as new_file:
        (
            new_file.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            if os.path.getsize(file_path) == 0
            else new_file.write(
                f"\n\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
        )
        content_line_order_number = 0
        while True:
            content_line_order_number += 1
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            new_file.write(f"\n{content_line_order_number} {content}")


def main() -> None:
    commands = sys.argv
    process_terminal = process_terminal_input(commands)
    if process_terminal is not None:
        create_file_or_write_into_it(process_terminal)


if __name__ == "__main__":
    main()
