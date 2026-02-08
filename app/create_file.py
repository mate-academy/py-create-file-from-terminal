import sys
import os
import datetime


def handle_command() -> None:
    command = sys.argv
    has_d = "-d" in command
    has_f = "-f" in command
    if has_d and not has_f:
        d_index = command.index("-d")
        dir_parts = command[d_index + 1 :]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    elif has_f and not has_d:
        f_index = command.index("-f")
        file_name = command[f_index + 1]

        make_file(file_name)

    elif has_f and has_d:
        f_index = command.index("-f")
        file_name = command[f_index + 1]
        d_index = command.index("-d")
        if d_index > f_index:
            p_dir = command[d_index + 1 :]
        else:
            p_dir = command[d_index + 1 : f_index]
        dir_path = os.path.join(*p_dir)
        dir_path_with_file = os.path.join(dir_path, file_name)
        os.makedirs(dir_path, exist_ok=True)
        make_file(dir_path_with_file)


def make_file(path_or_file: str) -> None:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path_or_file, "a") as f:
        f.write(f"{current_time}\n")
        counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{counter} {line}\n")
            counter += 1
        f.write("\n")


handle_command()
