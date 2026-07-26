import os
import sys
from datetime import datetime


def parse_terminal() -> None:
    terminal = sys.argv
    terminal.pop(0)
    path = ""
    if "-d" in terminal:
        path = create_dir(terminal)

    if "-f" in terminal:
        create_notation(terminal, path)


def create_dir(terminal: list) -> str:
    path = []
    for index in range(1, len(terminal)):
        if terminal[index] == "-f":
            break
        path.append(terminal[index])
    path = os.path.join(*path)
    os.makedirs(path, mode=0o777, exist_ok=True)
    return path


def create_notation(terminal: list, path: str = None) -> None:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = f"{current_date}\n"
    count = 0
    while True:
        count += 1
        last_text = input("Enter content line: ")
        if last_text == "stop":
            break
        text += f"{count} " + last_text + "\n"
    text = text.rstrip()
    if path:
        new_path = os.path.join(path, terminal[-1])
    else:
        new_path = terminal[-1]
    if os.path.exists(new_path):
        text = "\n\n" + text
    with open(new_path, "a") as new_file:
        new_file.write(text)


def main() -> None:
    parse_terminal()


if __name__ == "__main__":
    main()
