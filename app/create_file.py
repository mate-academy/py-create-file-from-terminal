import sys
import os
import datetime


def get_directory_list(command_list: list) -> list[str] | None:
    if command_list.index("-d") < len(command_list) - 1:
        return commands[commands.index("-d") + 1: commands.index("-f") | 0]


def get_file_name(command_list: list[str]) -> str | None:
    if command_list.index("-f") < len(command_list) - 1:
        return command_list[command_list.index("-f") + 1]


def create_directories(path: list[str], command_list: list[str]) -> None:
    if directory_list := get_directory_list(command_list):
        for directory in directory_list:
            path[0] = os.path.join(path[0], directory)
            os.makedirs(path[0], exist_ok=True)


def create_file(path: list[str], command_list: list[str]) -> None:
    time_now = datetime.datetime.now()

    if file_name := get_file_name(command_list):
        with open(os.path.join(path[0], file_name), "a") as file_in:
            file_in.writelines(f"{time_now.strftime('%Y-%m-%d %X')}\n")
            count = 1

            while True:
                user_input = input("content line: ")
                if user_input != "stop":
                    file_in.writelines(f"{count} {user_input}\n")
                    count += 1
                else:
                    file_in.writelines("\n")
                    break


if __name__ == "__main__":
    commands = sys.argv
    final_path = [os.getcwd()]
    if "-d" in commands:
        create_directories(path=final_path, command_list=commands)
    if "-f" in commands:
        create_file(path=final_path, command_list=commands)
