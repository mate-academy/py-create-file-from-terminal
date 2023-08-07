#! python

import datetime
import os
import sys

DIRS, FILE = "-d", "-f"


def tokenize_command(command: list) -> dict:
    global DIRS, FILE
    tokens, realize_info = {}, 1
    if DIRS in command:
        tokens[DIRS] = command[command.index(DIRS) + realize_info:]
    if FILE in command:
        tokens[FILE] = command[command.index(FILE) + realize_info]
    return tokens


def create_dirs(dirs: list[str]) -> str:
    directories = os.path.sep.join(dirs)
    path = os.path.abspath(os.path.join(os.path.curdir,
                                        directories))
    os.makedirs(path, exist_ok=True)
    return path


def create_and_write_file(file_name: str,
                          path: str = os.path.abspath(
                              os.path.join(os.path.curdir)
                          )) -> None:
    text = ""
    file_path = os.path.join(path, file_name.strip())
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_line = current_time + "\n"
    time_mark = "\n" + time_line if os.path.exists(file_path) else time_line
    line = 1
    while True:
        edit_text = input("Enter content line: ")
        if edit_text == "stop":
            break
        text += f"{line} {edit_text} \n"
        line += 1
    with open(f"{file_path}", "a") as file:
        file.write(time_mark)
        file.write(text)


def run_cmd_commands() -> None:
    global DIRS, FILE
    command = sys.argv
    tokens = tokenize_command(command=command)
    plots = {
        DIRS: create_dirs,
        FILE: create_and_write_file,
    }
    if DIRS in tokens and FILE in tokens:
        path = create_dirs(tokens[DIRS])
        create_and_write_file(tokens[FILE], path)
    else:
        for flag in tokens:
            plots[flag](tokens[flag])


if __name__ == "__main__":
    run_cmd_commands()
