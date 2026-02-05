from sys import argv
import os
from datetime import datetime


def make_directions(new_director: list) -> str:
    path_to_new_dir = os.path.join(*new_director)
    if not os.path.exists(path_to_new_dir):
        os.makedirs(path_to_new_dir)
    return path_to_new_dir


def make_file(file_name: str) -> None:
    with open(file_name, "a") as new_file:
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(f"{time_stamp}\n")
        line_num = 1
        while True:
            content = input("Enter content here ->")
            if content == "stop":
                break
            new_file.write(f"Line{line_num} {content}\n")
            line_num += 1


def starter() -> None:
    command = argv[1:]
    if "-d" in command and "-f" in command:
        directions = command[command.index("-d") + 1: command.index("-f")]
        path_dir = make_directions(directions)
        file_path = os.path.join(path_dir, f"{command[-1]}")
        make_file(file_path)

    if "-d" in command and "-f" not in command:
        make_directions(command[command.index("-d") + 1:])

    if "-f" in command and "-d" not in command:
        make_file(command[-1])


if __name__ == "__main__":
    starter()
