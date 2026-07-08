import sys
import os
import datetime


def reading_terminal_command() -> None:
    terminal_command = sys.argv
    has_d = "-d" in terminal_command
    has_f = "-f" in terminal_command

    path = []
    if has_d:
        d_idx = terminal_command.index("-d")
        for item in terminal_command[d_idx + 1:]:
            if item == "-f":
                break
            path.append(item)
    target_dir = "/".join(path) if path else ""
    file_name = ""
    if has_f:
        f_idx = terminal_command.index("-f")
        file_name = terminal_command[f_idx + 1]
    elif not has_d:
        file_name = terminal_command[-1]
    if target_dir:
        create_directory(target_dir)
    if file_name:
        create_file_with_text(file_name, target_dir)


def create_directory(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)


def create_file_with_text(name: str, directory: str = "") -> None:
    full_path = os.path.join(directory, name) if directory else name
    prefix = ""
    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
        prefix = "\n"
    with open(full_path, "a") as f:
        if prefix:
            f.write(prefix)
        current_time = datetime.datetime.now()
        f.write(current_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line.lower() == "stop":
                break
            f.write(str(line_number) + " " + new_line + "\n")
            line_number += 1


reading_terminal_command()
