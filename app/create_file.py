import sys
import os
from datetime import datetime


def write_text_to_file(file_name):
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        content = input("Enter content line: ")
        n = 0
        while content != "stop":
            text = f"Line{n + 1} {content}\n"
            f.write(text)
            content = input("Enter content line: ")


def create_file_from_terminal():
    command = sys.argv
    if "-f" not in command:
        for i in range(2, len(command) - 1):
            os.mkdir(command[i])
    if "-d" not in command:
        write_text_to_file(command[-1])
    if "-d" in command and "-f" in command:
        for i in range(2, len(command) - 2):
            os.mkdir(command[i])
        write_text_to_file(command[-1])
