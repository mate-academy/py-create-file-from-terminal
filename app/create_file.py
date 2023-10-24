import sys
import os
from datetime import datetime
from typing import List


def create_dirs(dirs: List[str]) -> str:
    if not os.path.exists("/".join(dirs)):
        os.makedirs("/".join(dirs))
    return "/".join(dirs)


def create_file(name: str, directory: str = "") -> None:
    line = input("Enter content line: ")
    time = datetime.now()
    content = time.strftime("%Y-%m-%d %H:%M:%S\n")
    line_number = 1
    while line != "stop":
        content += f"{line_number} {line}\n"
        line = input("Enter content line: ")
        line_number += 1
    with open(directory + "/" + name, "a") as file:
        file.write(content)


def normalize_commands(terminal_passed: List[str]) -> tuple:
    d_value = None
    f_value = None

    if "-f" in terminal_passed:
        index_of_f = terminal_passed.index("-f")
        f_value = terminal_passed[index_of_f + 1]
    if "-d" in terminal_passed:
        index_of_d = terminal_passed.index("-d")
        if f_value:
            d_value = terminal_passed[index_of_d + 1:index_of_f]
        else:
            d_value = terminal_passed[index_of_d + 1:]
    return {"-d": d_value, "-f": f_value}


commands = normalize_commands(sys.argv)
if commands["-d"] and not commands["-f"]:
    create_dirs(commands["-d"])
if not commands["-d"] and commands["-f"]:
    create_file(commands["-f"])
if commands["-d"] and commands["-f"]:
    create_file(commands["-f"], create_dirs(commands["-d"]))
