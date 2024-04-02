import os
import sys
from datetime import datetime


def input_from_console() -> str:
    content = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    count = 1
    while True:
        input_text = input("Enter content line:")
        if input_text.lower() == "stop":
            break
        content += "\n" + str(count) + " " + input_text
        count += 1
    return content


def create_dir(terminal: list) -> str:
    path = []
    for index in range(len(terminal)):
        if terminal[index] == "-f":
            break
        path.append(terminal[index])
    path = os.path.join(*path)
    os.makedirs(path, mode=0o777, exist_ok=True)
    return path


def create_file(terminal: list, path: str = None) -> None:
    text = input_from_console()
    if path:
        new_path = os.path.join(path, terminal[-1])
    else:
        new_path = terminal[-1]
    if os.path.exists(new_path):
        text = f"\n{'-' * 25}\n{text}"
    with open(new_path, "a") as new_file:
        new_file.write(text)


def terminal() -> None:
    terminal_input = sys.argv[1::]
    path = ""
    if "-d" in terminal_input:
        path = create_dir(terminal_input[1::])
    if "-f" in terminal_input:
        create_file(terminal_input, path)


if __name__ == "__main__":
    terminal()
