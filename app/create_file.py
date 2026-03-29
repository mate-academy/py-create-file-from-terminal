from datetime import datetime
import os
import sys


def create_directory(dirs: str) -> None:
    dirs_path = os.path.join(dirs)
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
    index_d, index_f = [-1, -1]
    dirs, filename = ["", ""]
    command_list = sys.argv[1:]

    if "-f" in command_list:
        index_f = command_list.index("-f")
        filename = command_list[index_f + 1]

    if "-d" in command_list:
        index_d = command_list.index("-d")
        dirs = "/".join(command_list[index_d + 1:])
        if index_f > index_d:
            dirs = "/".join(command_list[index_d + 1:index_f])

    if dirs != "":
        create_directory(dirs)
    if filename != "":
        create_file(dirs, filename)


if __name__ == "__main__":
    start()
