from sys import argv
from os import path, makedirs
from datetime import datetime


def get_commands(commands: list) -> dict[str] | None:
    if "-f" not in commands:
        return
    index_f_flag = commands.index("-f")
    param = {"file_name": commands[index_f_flag + 1], "path": ""}

    if "-d" in commands:
        index_d_flag = commands.index("-d")
        end_index = index_f_flag if index_f_flag > index_d_flag else None
        param["path"] = path.join(*commands[index_d_flag + 1:end_index])

    return param


def write_to_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        i = 1
        while line_content := input("Enter content line: ") != "stop":
            f.write(f'{i} {line_content}\n')
            i += 1


if __name__ == '__main__':
    if len(argv) > 2:
        param = get_commands([arg.strip() for arg in argv])
        if param:
            if param["path"] and not path.isdir(param["path"]):
                makedirs(param["path"])
            write_to_file(path.join(param["path"], param["file_name"]))
