import os
import sys
import datetime


def parse_command() -> None:
    command = sys.argv[1:]
    filename = None
    path = None
    for index, item in enumerate(command):
        if item == "-f":
            filename = command.pop(index + 1)
            command.pop(index)
    if command:
        path = create_path(command[1:])
    if filename is not None and path is None:
        create_file(filename)
    if filename is not None and path is not None:
        create_file(path + "\\" + filename)


def create_file(filename: str) -> None:
    print(f"Create file {filename}")
    user_input = handle_cli()
    with open(filename, "a") as file:
        file.write(user_input)


def create_path(path: list) -> str:
    path = os.path.join(*path)
    os.makedirs(path, exist_ok=True)
    return path


def handle_cli() -> str:
    time = datetime.datetime.now()
    result = time.strftime("%Y-%m-%d %H:%M:%S") + "\n"
    cnt = 1
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            result += "\n"
            break
        result += f"{cnt} {user_input}\n"
        cnt += 1
    return result


if __name__ == "__main__":
    parse_command()
