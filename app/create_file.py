import sys
import os
from datetime import datetime


def create_file(name_file: str) -> None:
    with open(name_file, "a") as file:
        file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S") + "\n")
        count = 1
        while True:
            text = input("Enter content line:")
            if text.lower() == "stop":
                file.write("\n")
                break
            file.writelines(f"{count} {text}\n")
            count += 1


def parse_sys_argv(command: list) -> dict:
    check_flag_f = command.index("-f") if "-f" in command else None
    check_flag_d = command.index("-d") if "-d" in command else None
    result = {"path": None, "name_file": None}

    if (check_flag_f is not None) and (check_flag_d is not None):

        if check_flag_d < check_flag_f:
            result["path"] = "\\".join(command[check_flag_d + 1: check_flag_f])
        else:
            result["path"] = "\\".join(command[check_flag_d + 1:])

        result["name_file"] = command[check_flag_f + 1]

    elif check_flag_d is not None:
        new_path = command[command.index("-d") + 1:]
        result["path"] = "\\".join(new_path)

    elif check_flag_f is not None:
        file_name = command[command.index("-f") + 1]
        result["name_file"] = file_name

    return result


if __name__ == "__main__":
    create_new_info = sys.argv
    file_info = parse_sys_argv(create_new_info)

    if not (
        file_info["path"] is None
        or os.path.exists(f"{os.getcwd()}\\{file_info["path"]}")
    ):
        os.makedirs(file_info["path"])

    if file_info["path"] is not None:
        os.chdir(file_info["path"])

    if file_info["name_file"] is not None:
        create_file(file_info["name_file"])
