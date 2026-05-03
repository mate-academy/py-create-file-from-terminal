from sys import argv
from os import makedirs, path
from datetime import datetime
from typing import Any


def parse_arguments(arg_list: list) -> dict:
    parsed_dict = {
        "filename": "",
        "directory": [],
        "flag_f": False,
        "flag_d": False,
        "info": ""
    }

    if len(argv) <= 2:
        parsed_dict["info"] = "Usage: -f <filename> or/and -d <directory>"
        return parsed_dict

    for index in range(len(arg_list)):
        if arg_list[index] == "-f":
            try:
                parsed_dict["filename"] = arg_list[index + 1]
                del arg_list[index: index + 2]
                parsed_dict["flag_f"] = True
                break
            except IndexError:
                parsed_dict["info"] = "No filename"
                return parsed_dict

    for index in range(len(arg_list)):
        if arg_list[index] == "-d":
            if index == len(arg_list) - 1:
                parsed_dict["info"] = "No directory name(s)"
                return parsed_dict
            parsed_dict["directory"] = [name for name in arg_list[index + 1:]]
            parsed_dict["flag_d"] = True
            break

    return parsed_dict


def get_content() -> list:
    content = []
    stop = False
    line_number = 1

    while not stop:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            stop = True
        else:
            content.append(f"\n{line_number} {line}")
            line_number += 1

    return content


def wright_content(content: list, file_path: str) -> None:
    new_line = "\n\n" if path.isfile(file_path) else ""

    with open(file_path, "a") as f:
        f.write(new_line + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for line in content:
            f.write(line)


def create_file() -> Any:

    arguments = parse_arguments([arg.strip() for arg in argv[1:]])
    print(arguments)
    if arguments["info"] != "":
        return

    if arguments["flag_d"]:
        makedirs(path.join(*arguments["directory"]), exist_ok=True)

    if arguments["flag_f"]:
        full_path = path.join(*arguments["directory"], arguments["filename"])

        content = get_content()
        wright_content(content, full_path)


create_file()
