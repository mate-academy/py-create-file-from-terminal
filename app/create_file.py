import sys
import os
import datetime


def accept_list_from_terminal_and_make_dirs(commands: list):
    itinerary = None
    if len(commands) > 3:
        itinerary = "/".join(commands[2:])
    if len(commands) == 3:
        itinerary = commands[2]
    os.makedirs(itinerary)
    return itinerary


def accept_list_from_terminal_and_return_file(file: str):
    with open(file, "a") as f:
        f.write(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        while content != "stop":
            content = input("Enter content line:")
            if content != "stop":
                f.write(content)


information = sys.argv
if information[1] == "-d" and information[-2] != "-f":
    accept_list_from_terminal_and_make_dirs(information)
if information[1] == "-f":
    path = information[2]
    accept_list_from_terminal_and_return_file(path)
if information[1] == "-d" and information[-2] == "-f":
    path = accept_list_from_terminal_and_make_dirs(information)
    create_file = f"{path}/{information[-1]}"
    accept_list_from_terminal_and_return_file(create_file)
