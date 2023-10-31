import datetime
import os
import sys


def create_path(command: list) -> None:
    path = ""
    if command[1] == "-d":
        directory_path = command[2:] if "-f" != command[-2] else command[2:-2]
        path = os.path.join(*directory_path)
    elif command[1] == "-f" and "-d" in command:
        path = os.path.join(*command[4:])

    if path:
        os.makedirs(path, exist_ok=True)

    if "-f" in command:
        path = os.path.join(path, command[command.index("-f") + 1])
        main(path)


def main(file_path: str) -> None:
    num_index = 0
    content = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    while True:
        num_index += 1
        message = input("Enter content line: ")
        if message == "stop":
            break
        content += f"{num_index} {message}\n"
    content += "\n"

    with open(file_path, "a") as file:
        file.write(content)


if __name__ == "__main__":
    create_path(sys.argv)
