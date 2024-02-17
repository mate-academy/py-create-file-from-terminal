from datetime import datetime
import os
import sys


def create_directory(dirs: str) -> None:
    dirs_path = os.path.join(dirs)
    if not os.path.isdir(dirs_path):
        os.makedirs(dirs_path, exist_ok=True)


def create_file(dirs: str, filename: str) -> None:
    now = datetime.now()
    text = now.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    num_line = 1

    while True:
        line_content = input("Enter new line of content: ")
        if line_content.lower() == "stop":
            break
        text += f"{num_line} {line_content} \n"
        num_line += 1
    text += "\n"

    file_path = os.path.join(dirs, filename)
    with open(file_path, "a") as file_out:
        file_out.write(text)


def start() -> None:
    command_list = " ".join(sys.argv[1:]).split("-")

    dirs, filename = ["", ""]
    for command in command_list[1:]:
        if command[0] == "d":
            dirs = command[1:].strip().replace(" ", "/")
        if command[0] == "f":
            filename = command[1:].strip()

    if dirs != "":
        create_directory(dirs)
    if filename != "":
        create_file(dirs, filename)


if __name__ == "__main__":
    start()
