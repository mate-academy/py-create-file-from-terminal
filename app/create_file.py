import os
import sys
import datetime


def read_command() -> str:
    terminal_commands = sys.argv
    command_count = len(terminal_commands)
    dirs = []
    dir_index = 0
    if "-d" in terminal_commands:
        dir_index = terminal_commands.index("-d")
    file_name = "file.txt"
    file_index = 0
    if "-f" in terminal_commands:
        file_index = terminal_commands.index("-f")
        if (
                file_index + 1 <= command_count - 1
        ) and (
                terminal_commands[file_index + 1]
        ) != "-d":
            file_name = terminal_commands[file_index + 1]
    if dir_index != 0:
        if dir_index > file_index:
            dirs = terminal_commands[dir_index + 1: command_count]
        else:
            dirs = terminal_commands[dir_index + 1: file_index]
    if dir_index != 0 and len(dirs) > 0 and file_index == 0:
        dir_path = os.path.join(*dirs)
        os.mkdir(dir_path)
        file_path = os.path.join(*dirs, file_name)
    else:
        file_path = file_name
    return file_path


def write_to_file(file_path: str) -> None:
    with open(file_path, "w") as file_:
        now = datetime.datetime.now()
        file_.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        index_line = 0
        while True:
            index_line += 1
            txt = input()
            if txt == "stop":
                break
            file_.write(str(index_line) + " " + txt + "\n")


if __name__ == "__main__":
    file_full_name = read_command()
    write_to_file(file_full_name)
