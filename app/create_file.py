import sys
from datetime import datetime


def is_create_dir_or_file(term_cmds_status: dir) -> bool:
    if not term_cmds_status["create_dir"] and not term_cmds_status["create_file"]:
        print("ERROR: No create_dir or create_file")
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


def main():
    terminal_cmds = sys.argv[1:]
    print(f"{terminal_cmds=}")
    cmds = is_terminal_cmds(terminal_cmds)
    print(f"{cmds=}")
    is_create_dir_or_file(cmds)
    dir_to_create = dir_from_cmds(terminal_cmds)
    print(f"{dir_to_create=}")


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
