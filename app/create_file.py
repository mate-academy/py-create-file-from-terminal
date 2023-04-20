import os
import sys
from datetime import datetime


def create_directories_path(command: str) -> str:
    start = command.index("-d") + 1
    end = None
    if "-f" in command and command.index("-d") < command.index("-f"):
        end = command.index("-f")
    return os.path.join(*command[start: end])


def create_file(path_to_file: str) -> None:
    mode = "a" if os.path.isfile(path_to_file) else "w"
    with open(path_to_file, mode) as file:
        now = datetime.now()
        file.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_content = None
        count = 1
        while line_content != "stop":
            line_content = input("Enter content line: ")
            if line_content != "stop":
                file.write(f"{count} {line_content}\n")
                count += 1
            else:
                file.write("\n")
        del count


if __name__ == "__main__":
    users_command = sys.argv
    if "-d" in users_command:
        dir_path = create_directories_path(users_command)
        os.makedirs(dir_path, exist_ok=True)
    if "-f" in users_command:
        filename = users_command[users_command.index("-f") + 1]
        if "-d" in users_command:
            filename = os.path.join(dir_path, filename)
        create_file(filename)
