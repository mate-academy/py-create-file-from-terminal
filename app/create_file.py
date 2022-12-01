import sys
import os
from datetime import datetime


def accept_list_from_terminal_and_make_dirs(commands: list) -> str:
    itinerary = None
    if len(commands) > 3:
        itinerary = "/".join(commands[2:])
    if len(commands) == 3:
        itinerary = commands[2]
    os.makedirs(itinerary)
    return itinerary


def accept_list_from_terminal_and_return_file(new_file: str) -> None:
    content = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    content_for_new_file = f"{content}"
    while content != "stop":
        content = input("Enter content line:")
        if content != "stop":
            content_for_new_file += f"\n{content}"
    with open(new_file, "a") as f:
        f.write(content_for_new_file)


commands_from_terminal = sys.argv
if commands_from_terminal[1] == "-d" and commands_from_terminal[-2] != "-f":
    accept_list_from_terminal_and_make_dirs(commands_from_terminal)
if commands_from_terminal[1] == "-f":
    name_for_file = commands_from_terminal[2]
    accept_list_from_terminal_and_return_file(name_for_file)
if commands_from_terminal[1] == "-d" and commands_from_terminal[-2] == "-f":
    file_path = accept_list_from_terminal_and_make_dirs(commands_from_terminal)
    name_for_file = f"{file_path}/{commands_from_terminal[-1]}"
    accept_list_from_terminal_and_return_file(name_for_file)
