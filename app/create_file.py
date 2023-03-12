import sys
from datetime import datetime
import os


def create_file_from_terminal() -> str:
    command = sys.argv
    if "-d" not in command[1]:
        path = os.path.join(str(os.getcwd()), command[3])
        os.makedirs(path, exist_ok=True)
    else:
        path = os.path.join(command[4], command[5])
        os.makedirs(path, exist_ok=True)
    add_content(path)


def add_content(path: str) -> None:
    create_file_from_terminal()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(f"{path}", "w") as file:
        file.write(timestamp + '\n')
    while True:
        line_number = 1
        input_content = f"{str(line_number)} {input('Enter content line: ')}"
        with open(f"{path}", "w") as file:
            file.write(f"{input_content} '\n'")
        line_number += 1
        if "stop" in input_content:
            break


if __name__ == "__main__":
    create_file_from_terminal()
