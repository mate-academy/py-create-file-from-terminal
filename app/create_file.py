import sys
import os
import datetime


def create_directory(command: list) -> str:
    if len(command) > 1 and command[0] == "-d":
        path_parts = command[1:]
        dir_path = os.path.join(os.getcwd(), *path_parts)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    else:
        pass


def create_file(command: list, file_path: str = os.getcwd()) -> None:
    if len(command) > 1 and command[0] == "-f":
        name_file = command[1]
        file_create_path = os.path.join(file_path, name_file)
        with open(file_create_path, "a", encoding="utf-8") as file:
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(date + "\n")
            sequence_number = 1
            sequence_line = 1
            while True:
                user_input = input("Enter content line: ")
                if user_input.lower() != "stop":
                    file.write(f"{sequence_number} "
                               f"Line{sequence_line} {user_input}" + "\n")
                    sequence_number += 1
                    sequence_line += 1
                else:
                    file.write("\n")
                    break


def process_command() -> None:
    commands = sys.argv
    if commands.count("-d") == 1 and commands.count("-f") == 1:
        index_create_file = commands.index("-f")
        commands_before_f = commands[1:index_create_file]
        path = create_directory(commands_before_f)
        commands_after_f = commands[index_create_file:]
        create_file(commands_after_f, path)
    elif commands[1] == "-d":
        create_directory(commands)
    elif commands[1] == "-f":
        create_file(commands)


process_command()
