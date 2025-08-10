import sys
import os
from datetime import datetime


def create_file(dirs: list[str], filename: str) -> None:
    filepath = ""
    if len(dirs):
        filepath = os.path.join(*dirs)
        os.makedirs(filepath, exist_ok=True)
    if filename:
        filepath = os.path.join(filepath, filename)

        with open(filepath, "a") as a:
            a.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            user_data_line = input("Enter content line: ")
            counter = 1

            while user_data_line.lower() != "stop":
                a.write(f"{counter} {user_data_line}\n")
                counter += 1
                user_data_line = input("Enter content line: ")

            a.write("\n")


def create_list_dirs(commands: list[str]) -> list[str]:
    try:
        return commands[:commands.index("-f")]
    except ValueError:
        return commands


terminal_commands = sys.argv[1:]


def main() -> None:
    if "-d" in terminal_commands and "-f" in terminal_commands:
        user_file = terminal_commands[terminal_commands.index("-f") + 1:][0]

        dirs = create_list_dirs(
            terminal_commands[terminal_commands.index("-d") + 1:]
        )
        create_file(dirs, user_file)
    elif "-d" in terminal_commands:
        dirs = create_list_dirs(
            terminal_commands[terminal_commands.index("-d") + 1:]
        )
        create_file(dirs, "")
    elif "-f" in terminal_commands:
        user_file = terminal_commands[terminal_commands.index("-f") + 1:][0]
        create_file([], user_file)
    else:
        create_file(["dir1", "dir2"], "file.txt")


if __name__ == "__main__":
    main()
