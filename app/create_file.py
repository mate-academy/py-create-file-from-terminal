import os
import sys

from app.append_to_file import append_content
from app.create_file_with_content import create_file_with_content


def create_file():
    com1, com2 = "-d", "-f"
    command = sys.argv
    if com1 in command and com2 in command:
        path = "/".join(command[command.index(com1) + 1: command.index(com2)])
        os.makedirs(path)
        create_file_with_content(command)
    if com1 in command:
        path = "/".join(command[(command.index(com1) + 1):])
        os.makedirs(path)
    if com2 in command:
        if os.path.exists(command[-1]):
            append_content(command)
        else:
            create_file_with_content(command)
