import sys
import os
import datetime


def create_and_write_into_file(file_name: str) -> None:
    current_date = datetime.datetime.now()
    text = []
    line_number = 1
    while True:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        text.append(f"{line_number} {new_line}\n")
        line_number += 1
    with open(file_name, "a") as source_file:
        source_file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        source_file.writelines(text)
        source_file.write("\n")


def handle_command() -> None:
    commands = sys.argv
    if "-d" in commands and "-f" in commands:
        d_index, f_index = commands.index("-d"), commands.index("-f")
        path = commands[d_index + 1]
        os.makedirs(path, exist_ok=True)
        stop_index = f_index if d_index < f_index else len(commands)
        for i in range(d_index + 2, stop_index):
            path = os.path.join(path, commands[i])
            os.makedirs(path, exist_ok=True)
        path = os.path.join(path, commands[f_index + 1])
        create_and_write_into_file(path)
    elif "-f" in commands:
        f_index = commands.index("-f")
        create_and_write_into_file(commands[f_index + 1])
    elif "-d" in commands:
        d_index = commands.index("-d")
        path = commands[d_index + 1]
        os.makedirs(path, exist_ok=True)
        for i in range(d_index + 2, len(commands)):
            path = os.path.join(path, commands[i])
            os.makedirs(path, exist_ok=True)


if __name__ == "__main__":
    handle_command()
