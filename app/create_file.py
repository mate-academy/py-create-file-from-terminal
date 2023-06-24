import os
import sys
from datetime import datetime


def create_file() -> None:
    terminal_command = sys.argv
    file_name = terminal_command[terminal_command.index("-f") + 1]
    directory_name = ""

    if "-d" in terminal_command:
        for argument in terminal_command[terminal_command.index("-d") + 1:]:
            if argument == "-f":
                break
            directory_name = os.path.join(directory_name, argument)
        os.makedirs(directory_name, exist_ok=True)

    if "-f" in terminal_command:
        with open(os.path.join(directory_name, file_name), "a+") as new_file:
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


if __name__ == "__main__":
    create_file()
