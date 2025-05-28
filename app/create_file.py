import os
import sys
import datetime


def create_directory(path: str):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print(f"Error: {error}")
        sys.exit(1)

time_now = datetime.datetime.now()

def create_file(name_file: str):
    if not os.path.exists(name_file):
        with open(name_file, "a") as file:
            file.write(f"{time_now.strftime('%y-%m-%d %H:%M:%S')}\n")
            counter_lines = 0
            while True:
                text = input("Enter content line:")
                counter_lines += 1
                if text.lower() == "stop":
                    break
                file.write(f"Line {counter_lines} content: {text} \n")
        return
    with open(name_file, "w") as file:
        file.write(f"{time_now.strftime('%y-%m-%d %H:%M:%S')}\n")
        counter_lines = 0
        while True:
            text = input("Enter content line:")
            counter_lines += 1
            if text.lower() == "stop":
                break
            file.write(f"Another line {counter_lines} content: {text} \n")

def create_file_or_directory() -> None:
    command_terminal = sys.argv
    cwd_dir = os.getcwd()

    if "-d" in command_terminal and "-f" not in command_terminal:
        list_d = []
        index_directory = command_terminal[command_terminal.index("-d") + 1:]
        for index in index_directory:
            list_d.append(index)
        path_directory = os.path.join(*list_d)
        create_directory(path_directory)
        sys.exit(1)

    if "-f" in command_terminal and "-d" not in command_terminal:
        index_file = command_terminal[command_terminal.index("-f") + 1:]
        path_file = os.path.join(cwd_dir, index_file[0])
        create_file(path_file)
    if "-f" in command_terminal and "-d" in command_terminal:
        path_directory = command_terminal[command_terminal.index("-d") + 1: command_terminal.index("-f")]
        file_index = command_terminal[command_terminal.index("-f") + 1:]
        list_direct = []
        for directories in path_directory:
            list_direct.append(directories)
        path_d = os.path.join(*list_direct)
        create_directory(path_d)

        path_f = os.path.join(path_d, file_index[0])
        create_file(path_f)


if __name__ == "__main__":
    create_file_or_directory()