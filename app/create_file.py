import sys
import datetime
import os


def make_file_directory(
        comm_list: list,
        name_direct: str,
        amount_argv: int
) -> str:
    if comm_list[1] == "-d":
        for item in range(2, amount_argv):
            if comm_list[item] == "-f":
                break
            name_direct = name_direct + "/" + str(sys.argv[item])
            os.mkdir(name_direct)
    return name_direct


def write_to_file(comm_list: list, name_direct: str) -> None:
    now = datetime.datetime.now()
    with open(f"{name_direct}/{comm_list[-1]}", "w") as f:
        f.write(f"{now.date()} {now.hour}:{now.minute}:{now.second}\n")
        for line in sys.stdin:
            if "stop" != line.rstrip():
                print(f"Enter content line: {line}")
                f.write(line)
                continue
            break


def main_function() -> None:
    command_list = sys.argv
    if len(command_list) > 2:
        amount_of_argv = len(command_list)
        path_name = sys.path[0]
        name_dir = make_file_directory(
            command_list,
            path_name,
            amount_of_argv
        )
        for i in range(1, amount_of_argv):
            if command_list[i] == "-f":
                write_to_file(command_list, name_dir)


if __name__ == "__main__":
    main_function()
