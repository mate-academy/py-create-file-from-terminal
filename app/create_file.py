from datetime import datetime
import sys
import os


def parse_commands() -> dict:

    cmd = sys.argv
    data = {"file_name": None,
            "path": None}

    if "-f" in cmd:
        data["file_name"] = cmd[cmd.index("-f") + 1]

    if "-d" in cmd:
        data["path"] = "/".join(cmd[cmd.index("-d") + 1:])

    if "-f" in cmd and "-d" in cmd:
        data["path"] = data["path"][:data["path"].index("-f")]

    return data


def create_path(path: str) -> None:
    try:
        os.makedirs(path)

    except:
        pass


def create_file(name: str, path: str = "") -> None:
    with open(path + name, "w") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time}\n")
        line_number = 1
        content_line = input("Enter content line: ")
        while content_line != "stop":
            file.write(f"{line_number} Line{line_number} {content_line}\n")
            line_number += 1
            content_line = input("Enter content line: ")


def run_console() -> None:
    commands = parse_commands()
    if commands["file_name"] and commands["path"]:
        create_path(commands["path"])
        create_file(commands["file_name"], commands["path"])

    elif commands["file_name"]:
        create_file(commands["file_name"])

    elif commands["path"]:
        create_path(commands["path"])


run_console()
