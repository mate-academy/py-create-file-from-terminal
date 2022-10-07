import os
import sys

from datetime import datetime


def create_content(text: str) -> None:
    with open(text, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        content = int("Enter content line: ")
        i = 1
        while content != "stop":
            f.write(f"Line{i} {content}\n")
            content = int("Enter content line: ")


def create_file() -> None:
    commands = sys.argv
    if "-f" and "-d" in commands:
        for i in range(2, len(commands) - 2):
            os.makedirs(commands[i])
        create_content(commands[-1])
    if "-f" not in commands:
        for i in range(2, len(commands), -1):
            os.makedirs(commands[i])
    if "-d" not in commands:
        create_content(commands[-1])
