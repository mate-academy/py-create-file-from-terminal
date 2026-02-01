import os
import sys
from datetime import datetime
from typing import LiteralString


def is_create_dir_or_file(term_cmds_status: dir) -> None:
    if (not term_cmds_status["create_dir"]
            and not term_cmds_status["create_file"]):
        input("ERROR: No create_dir or create_file.\n"
              "Press 'Enter' button for an exit.")
        exit()


def is_terminal_cmds(terminal_commands: list[str]) -> dict:
    return_val = {"create_dir": False,
                  "create_file": False}

    if "-d" in terminal_commands:
        return_val["create_dir"] = True
    if "-f" in terminal_commands:
        return_val["create_file"] = True
    return return_val


def dir_from_cmds(cmds: list[str]) -> bool | list[str]:
    if "-d" not in cmds:
        print("ERROR: -d not in cmds")
        return False
    if "-f" not in cmds:
        cmds.remove("-d")
        return cmds
    d_origin = cmds.index("-d")
    f_origin = cmds.index("-f")
    return cmds[d_origin + 1: f_origin]


def create_local_path(dir_path_list: list) -> LiteralString | str | bytes:
    if len(dir_path_list) == 0:
        input("The folder name was not written.\n"
              "Press 'Enter' button for an exit.")
        exit()
    return os.path.join(*dir_path_list)


def file_name_from_cmds(cmds: list[str]) -> str:
    try:
        f_origin = cmds.index("-f")
        return cmds[f_origin + 1]
    except (IndexError, ValueError):
        input("The file name was not written.\n"
              "Press 'Enter' button for an exit.")
        exit()


def crate_dir(dir_path_list: list[str]) -> None:
    dir_path = create_local_path(dir_path_list)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"The '{dir_path}' where created.")
    else:
        print(f"The '{dir_path}' already exists.")


def write_to_file(file_path: LiteralString, value: str = "" | list) -> None:
    with open(file_path, "a") as file_to_write:
        file_to_write.write(value)


def get_content_from_client() -> list[str]:
    content_as_list = []
    i = 1
    while True:
        input_content = input("Enter content line: ")
        if input_content == "stop":
            break
        content_as_list.append(f"{i} {input_content}")
        i += 1

    return content_as_list


def main() -> None:
    print("""
    Hello, for create folder use template:
    -d <folder1 name> <folder2 name>.

    For create file use template:
    -f <folder1 name> <folder2 name>.

    For create folder and file use template:
    -d <folder1 name> <folder2 name> -f <folder1 name> <folder2
    """)
    terminal_cmds = sys.argv[1:]
    cmds = is_terminal_cmds(terminal_cmds)
    is_create_dir_or_file(cmds)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if cmds["create_dir"] and not cmds["create_file"]:
        dir_to_create = dir_from_cmds(terminal_cmds)
        crate_dir(dir_to_create)
        exit()

    if not cmds["create_dir"] and cmds["create_file"]:
        file_to_create = file_name_from_cmds(terminal_cmds)
        write_to_file(file_to_create)
        get_content = get_content_from_client()
        value_to_write = "\n".join([current_time] + get_content + ["\n"])
        write_to_file(file_to_create, value_to_write)
        print(f"The content added to the file '{file_to_create}'.")
        exit()

    if cmds["create_dir"] and cmds["create_file"]:
        file_to_create = file_name_from_cmds(terminal_cmds)
        dir_to_create = dir_from_cmds(terminal_cmds)
        local_path_file = create_local_path(dir_to_create + [file_to_create])
        crate_dir(dir_to_create)
        write_to_file(local_path_file)
        get_content = get_content_from_client()
        value_to_write = "\n".join([current_time] + get_content + ["\n"])
        write_to_file(local_path_file, value_to_write)
        print(f"The content added to the file '{file_to_create}'.")


if __name__ == "__main__":
    main()
