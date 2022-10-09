import sys
import datetime
import os


input_command = sys.argv


def create_dir(command: list) -> None:
    parent_dir = os.getcwd()
    for step in command:
        parent_dir = os.path.join(parent_dir, step)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    os.chdir(parent_dir)


def write_to_file(command: str) -> None:
    with open(f"{command}", "a") as f:
        f.write(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") + "\n")
        input_text = input("Enter content line:")
        while input_text != "stop":
            f.write(input_text + "\n")
            input_text = input("Enter content line:")
        f.write("\n")


if "-f" not in input_command:
    create_dir(input_command[2:])

if "-d" not in input_command:
    write_to_file(input_command[-1])

if "-d" in input_command and "-f" in input_command:
    create_dir(input_command[2:-2])
    write_to_file(input_command[-1])
