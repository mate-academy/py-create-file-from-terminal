#! python

import datetime
import os
import sys


def tokenize_command(flags: list, command: str) -> dict:
    currents = [flag for flag in command.split()
                if flag in flags]
    tokens, count = {}, 1
    for flag in currents:
        start_line = command.index(flag)
        flag_name = flag + " "
        if count < len(currents):
            end_line = command.index(currents[count])
            current_command = command[start_line: end_line - 1]
            tokens[flag] = current_command.replace(flag_name, "")
            command = command.replace(current_command, "")
        else:
            current_command = command[start_line:].strip()
            tokens[flag] = current_command.replace(flag_name, "")
        count += 1
    return tokens


def create_dirs(dirs: str) -> str:
    directories = os.path.sep.join(dirs.split())
    path = os.path.abspath(os.path.join(os.path.curdir, directories))
    os.makedirs(path, exist_ok=True)
    return path


def create_and_write_file(file_name: str,
                          path: str = os.path.abspath(
                              os.path.join(os.path.curdir)
                          )) -> None:
    text = ""
    file_path = os.path.join(path, file_name.strip())
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file_path):
        time_string = "\n" + current_time + "\n"
    else:
        time_string = current_time + "\n"
    with open(f"{file_path}", "a") as file:
        file.write(time_string)
    line = 1
    while True:
        edit_text = input("Enter content line: ")
        if edit_text == "stop":
            break
        text += f"{line} {edit_text} \n"
        line += 1
    with open(f"{file_path}", "a") as file:
        file.write(text)


command = " ".join(sys.argv[1:])

dirs_on_path, first_is_name = "-d", "-f"

tokens = tokenize_command(flags=[dirs_on_path,
                                 first_is_name],
                          command=command)

plots = {
    dirs_on_path: create_dirs,
    first_is_name: create_and_write_file,
}

if (dirs_on_path in tokens and first_is_name in tokens
        and command.index(dirs_on_path) < command.index(first_is_name)):
    path = plots[dirs_on_path](tokens[dirs_on_path])
    plots[first_is_name](tokens[first_is_name], path)

else:
    for flag in tokens:
        plots[flag](tokens[flag])

sys.exit()
