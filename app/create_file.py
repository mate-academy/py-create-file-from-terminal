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


def terminal(command_from_term: list) -> None:
    if command_from_term[1] == "-d" and command_from_term[-2] != "-f":
        accept_list_from_terminal_and_make_dirs(command_from_term)
    if command_from_term[1] == "-f":
        name_for_file = command_from_term[2]
        accept_list_from_terminal_and_return_file(name_for_file)
    if command_from_term[1] == "-d" and command_from_term[-2] == "-f":
        file_path = accept_list_from_terminal_and_make_dirs(command_from_term)
        name_for_file = f"{file_path}/{command_from_term[-1]}"
        accept_list_from_terminal_and_return_file(name_for_file)


command_from_terminal = sys.argv
terminal(command_from_terminal)
