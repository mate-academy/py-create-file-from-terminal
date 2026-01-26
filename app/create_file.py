import sys
import os
import datetime


def create_path() -> None:
    command = sys.argv
    if "-d" in command:
        d_index = command.index("-d")
        if "-f" in command:
            f_index = command.index("-f")
            if d_index < f_index:
                dir_path = os.path.join(*command[d_index + 1:f_index])
                file_path = os.path.join(*command[f_index + 1:])
            else:
                dir_path = os.path.join(*command[d_index + 1:])
                file_path = os.path.join(*command[f_index + 1: d_index])
            create_dir(dir_path)
            os.chdir(dir_path)
            create_file(file_path)
        else:
            dir_path = os.path.join(*command[d_index + 1:])
            create_dir(dir_path)

    if "-f" in command and "-d" not in command:
        f_index = command.index("-f")
        file_path = os.path.join(*command[f_index + 1:])
        create_file(file_path)


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    file_exists = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n\n")
        current_date = datetime.datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S"))
        number_line = 0
        while True:
            file_content = input("Enter content line: ")
            if file_content.lower() == "stop":
                break
            number_line += 1
            file.write(f"\n{number_line} {file_content}")


if __name__ == "__main__":
    create_path()
