from datetime import datetime
import os
import sys


def create_file_from_terminal() -> None:
    command = sys.argv
    path = None
    if "-f" == command[1] and "-d" not in command:
        path = os.path.join(str(os.getcwd()), command[-1])
    if "-d" in command:
        dir_path = (
            os.path.join(*command[2:-2])
            if "-f" == command[-2] else os.path.join(*command[2:])
        )
        os.makedirs(dir_path, exist_ok=True)
        if "-f" == command[-2]:
            path = os.path.join(str(os.getcwd()), dir_path, command[-1])
    if path is not None:
        add_content(path)


def add_content(path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_number = 0
    with open(f"{path}", "w") as file:
        file.write(timestamp + "\n")
        while True:
            line_number += 1
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file.write(f"line{str(line_number)} {line_content} \n")


if __name__ == "__main__":
    create_file_from_terminal()
