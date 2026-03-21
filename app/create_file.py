import sys
from datetime import datetime
import os


def create_file_from_console(command: str) -> None:
    if "-d" in command and "-f" not in command:
        dirs = command[command.find("-d") + 3:].replace(" ", "/")
        os.makedirs(dirs, exist_ok=True)

    elif "-f" in command and "-d" not in command:
        file_name = command[command.find("-f") + 3:].split()[0]

        content = file_exists(file_name)
        file_content_write(file_name, content)

    elif "-d" in command and "-f" in command:
        d_index = command.find("-d")
        f_index = command.find("-f")

        dirs = command[d_index + 3: f_index].replace(" ", "/")
        file_name = command[f_index + 3: ].split()[0]

        os.makedirs(dirs, exist_ok=True)

        content = file_exists(file_name)

        path = f"{dirs}{file_name}"
        file_content_write(path, content)


def file_exists(file_name: str) -> str:
    content = ""
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            content = f.read()
    return content


def file_content_write(path: str, content: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, "w") as f:
        if content:
            f.write(content)

        f.write(timestamp)
        count = 1
        while True:
            conn_line = input("Enter content line: ")
            if conn_line == "stop":
                break
            f.write(f"{count} {conn_line}")
            count += 1


if __name__ == "__main__":
    command_args = " ".join(sys.argv[1:])
    create_file_from_console(command_args)
