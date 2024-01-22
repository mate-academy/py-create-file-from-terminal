import os
import sys
from datetime import datetime


def get_clean_command(cmd: str) -> str:
    return " ".join(sys.argv).split(cmd)[1]


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        line = 1
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")
        while True:
            reply = input("Enter content line: ")
            if reply == "stop":
                file.write("\n")
                break
            file.write(f"{line} {reply}\n")
            line += 1


def path_operations() -> None:
    file_path, new_file = None, None

    if "-d" in sys.argv:
        command_dirs = get_clean_command("-d")
        if "-f" in command_dirs:
            command_dirs, new_file = command_dirs.split("-f")

        path = os.path.join(*command_dirs.split())
        os.makedirs(path, exist_ok=True)

        if new_file:
            file_path = os.path.join(path, new_file)
    elif "-f" in sys.argv:
        file_path = get_clean_command("-f")
    else:
        raise ValueError("No '-f' or '-d' command was passed!")

    if file_path:
        create_file(file_path)


if __name__ == "__main__":
    path_operations()
