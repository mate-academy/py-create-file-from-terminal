import sys
import os
import datetime


log = sys.argv


def verify_command(command: list) -> None:
    if command[1] == "-d":
        if "-f" in command:
            end_dir_idx = command.index("-f")
            path_dir = os.path.join(*command[2:end_dir_idx])
            os.makedirs(path_dir, exist_ok=True)
            full_path = os.path.join(path_dir, command[end_dir_idx + 1])
            create_fill_file(full_path)
        else:
            path = os.path.join(*command[2:])
            os.makedirs(path, exist_ok=True)
    elif command[1] == "-f" and len(log) == 3:
        create_fill_file(command[2])


def create_fill_file(path: str) -> None:
    with open(path, "w") as file:
        now = datetime.datetime.now()
        file.write(now.strftime("%a %-d %b %I:%M"))
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"\n{new_line}")


verify_command(log)
