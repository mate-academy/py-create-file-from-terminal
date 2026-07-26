import sys
import os
import datetime


def create_directory(command_arg: list[str]) -> str:
    start_path = command_arg.index("-d") + 1
    end_path = None
    if "-f" in command_arg:
        end_path = command_arg.index("-f")
    return os.path.join(*command_arg[start_path: end_path])


def create_file(path_to_file: str) -> None:
    if os.path.isfile(path_to_file):
        open_mode = "a"
    else:
        open_mode = "w"
    with open(path_to_file, open_mode) as new_file:
        date_time_now = datetime.datetime.utcnow()
        new_file.write(date_time_now.strftime("%Y-%m-%d %H:%M:%S" + "\n"))
        content = None
        line_number = 1
        while content != "stop":
            content = input("Enter content line: ")
            if content != "stop":
                new_file.write(f"{line_number} {content}" + "\n")
                line_number += 1
            else:
                new_file.write("\n")


if __name__ == "__main__":
    user_command = sys.argv
    if "-d" in user_command:
        path_dir = create_directory(user_command)
        os.makedirs(path_dir, exist_ok=True)
    if "-f" in user_command:
        file_name = user_command[user_command.index("-f") + 1]
        if "-d" in user_command:
            file_name = os.path.join(path_dir, file_name)
        create_file(file_name)
