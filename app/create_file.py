from sys import argv
from os import path, makedirs
from datetime import datetime


def is_param(index: int, commands: list) -> bool:
    return index < len(commands) and commands[index] not in ["-f", "-d"]


def get_commands(commands: list) -> dict[str]:
    param = {"-f": "", "-d": ""}

    if "-f" in commands:
        file_index = commands.index("-f") + 1
        if is_param(file_index, commands):
            param["-f"] = commands[file_index]

    if "-d" in commands:
        path_index = commands.index("-d") + 1
        while is_param(path_index, commands):
            param["-d"] = path.join(param["-d"], commands[path_index])
            path_index += 1

    return param


def create_directory(path_: str) -> None:
    if path_ and not path.isdir(path_):
        makedirs(path_)


def write_to_file(file_name: str, path_: str) -> None:
    if not file_name:
        return
    with open(path.join(path_, file_name), "a") as f:
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        i = 1
        while (line_content := input("Enter content line: ")) != "stop":
            f.write(f"{i} {line_content}\n")

            i += 1


def main() -> None:
    if len(argv) > 2:
        param = get_commands([arg.strip() for arg in argv])
        create_directory(param["-d"])
        write_to_file(param["-f"], param["-d"])


if __name__ == "__main__":
    main()
