import os
import sys
import datetime


if __name__ == "__main__":
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
        if (file_index + 1 <= command_count - 1) and terminal_commands[file_index + 1] != "-d":
            file_name = terminal_commands[file_index + 1]
    if dir_index != 0:
        if dir_index > file_index:
            dirs = terminal_commands[dir_index + 1: command_count]
        else:
            dirs = terminal_commands[dir_index + 1: file_index]
    if dir_index != 0 and len(dirs) > 0 and file_index == 0:
        os.mkdir(os.path.join(*dirs))

    with open(file_name, "r") as file_:
        while True:
            now = datetime.datetime.now()
            file_.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            txt = input()
            if txt == "stop":
                break
            file_.write(txt)
