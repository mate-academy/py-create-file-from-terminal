import sys
import os
from datetime import datetime


def create_file() -> None:
    terminal_command = sys.argv
    count = 0
    if "-d" in terminal_command:
        if "-f" in terminal_command:
            file_path = (
                "\\".join(terminal_command[
                          terminal_command.index("-d") + 1:
                          terminal_command.index("-f")]
                          )
            )
        else:
            file_path = "\\".join(terminal_command[2:])
        os.makedirs(file_path, exist_ok=True)
    if "-f" in terminal_command:
        if "-d" in terminal_command:
            path = os.path.join(file_path, terminal_command[
                terminal_command.index("-f") + 1
            ])
        else:
            path = terminal_command[terminal_command.index("-f") + 1]

        with open(path, "w") as file_name:
            file_name.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            content = ""
            while content != "stop":
                count += 1
                content = input("Enter content line:")
                file_name.write(f"{count} {content}\n")


create_file()
