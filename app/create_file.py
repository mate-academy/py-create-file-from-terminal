import sys
from datetime import datetime
import os


def create_file() -> None:
    command = sys.argv[1:]
    try:
        directory = command[command.index("-d") + 1:command.index("-f")]
    except ValueError:
        directory = []

    if "-d" in command:
        if "-f" in command:
            directory = command[command.index("-d") + 1:command.index("-f")]
        else:
            directory = command[command.index("-d") + 1:]
        os.makedirs("/".join(directory), exist_ok=True)

    if "-f" in command:
        file_name = command[command.index("-f") + 1:]
        with open("/".join(directory + file_name), "a") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            i = 1
            while True:
                words = input("Enter content line: ")
                if words == "stop":
                    break
                f.write("\n")
                f.write(f"{i} {words}")
                i += 1
            f.write("\n")


create_file()
