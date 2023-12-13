import sys
import os
import datetime

data_now = datetime.datetime.now()
current_data = data_now.strftime("%Y-%m-%d %H:%M:%S")


def write_in_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(current_data + "\n")
        length_file = 0
        while True:
            input_data = input("Enter content line: ")
            if input_data == "stop":
                break
            file.write(f"{length_file + 1} {input_data} \n")
        file.write("\n")


def create_file() -> None:
    command = sys.argv

    flag_f = command.index("-f")
    name_file = command[flag_f + 1]

    if "-f" in command and "-d" not in command:
        write_in_file(name_file)

    if "-d" in command and "-f" not in command:
        path_file = command[2:]
        os.makedirs(os.path.join(*path_file), exist_ok=True)

    if "-f" in command and "-d" in command:
        command.remove("-f")
        command.remove(name_file)
        path = command[2:]
        path_dirs = os.path.join(*path)
        os.makedirs(path_dirs, exist_ok=True)
        write_in_file(os.path.join(path_dirs, name_file))


if __name__ == "__main__":
    create_file()
