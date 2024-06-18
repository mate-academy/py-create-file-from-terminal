import os
import sys
from datetime import datetime
from typing import LiteralString


def is_create_dir_or_file(term_cmds_status: dir) -> None:
    if not term_cmds_status["create_dir"] and not term_cmds_status["create_file"]:
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


def dir_from_cmds(cmds: list[str]) -> list[str]:
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
    return os.path.join(*dir_path_list)


def file_name_from_cmds(cmds: list[str]) -> str:
    print(cmds)
    try:
        f_origin = cmds.index("-f")
        return cmds[f_origin + 1]
    except IndexError:
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


def create_file(file_name) -> None:
    # print(">create_file:")
    with open(file_name, "a") as file_to_write:
        file_to_write.write("")
    # print("<create_file:")


def main():
    terminal_cmds = sys.argv[1:]
    print(f"{terminal_cmds=}")
    cmds = is_terminal_cmds(terminal_cmds)
    print(f"{cmds=}")
    is_create_dir_or_file(cmds)
    if cmds["create_dir"] and not cmds["create_file"]:
        dir_to_create = dir_from_cmds(terminal_cmds)
        crate_dir(dir_to_create)
    if not cmds["create_dir"] and cmds["create_file"]:
        file_to_create = file_name_from_cmds(terminal_cmds)
        create_file(file_to_create)

    if cmds["create_dir"] and cmds["create_file"]:
        dir_to_create = dir_from_cmds(terminal_cmds)
        file_to_create = file_name_from_cmds(terminal_cmds)
        local_path_file = create_local_path(dir_to_create + [file_to_create])
        crate_dir(dir_to_create)
        create_file(local_path_file)

    # print(f"{file_to_create=}")
    # print(f"{dir_to_create=}")


# content_as_list = []
# current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
# while True:
#     input_content = input("Enter content line: ")
#     if input_content == "stop":
#         break
#     content_as_list.append(input_content)
#
# print(current_time)
# print(content_as_list)

if __name__ == "__main__":
    main()
