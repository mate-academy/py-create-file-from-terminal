import os
import sys
from datetime import datetime


def create_file() -> None:
    terminal_command = sys.argv

    directory = ""
    if "-d" in terminal_command:
        for argument in terminal_command[terminal_command.index("-d") + 1:]:
            if argument == "-f":
                break
            directory = os.path.join(directory, argument)
        os.makedirs(directory, exist_ok=True)

    if "-f" in terminal_command:
        with open(
                os.path.join(
                    directory,
                    terminal_command[terminal_command.index("-f") + 1]
                ),
                "a+"
        ) as new_file:
            new_file.seek(0)
            if new_file.readline():
                new_file.write("\n")
            new_file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S\n"))
            line_counter = 1
            while True:
                new_line = input("Enter content line: ")
                if new_line == "stop":
                    break
                new_file.write(f"{line_counter} {new_line}\n")
                line_counter += 1


create_file()
