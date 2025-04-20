import datetime
import os
import sys


def create_dirs(directories: list[str]) -> os.path:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str, dir_path: str = None) -> None:
    if dir_path:
        file_name = os.path.join(dir_path, file_name)

    with open(file_name, "a") as file:
        count = 0
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            line = input("Enter content line: ")
            count += 1
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{count} {line}\n")


def main_run() -> None:
    command_list = sys.argv
    try:
        if "-d" in command_list and "-f" in command_list:
            directory_path = create_dirs(
                command_list[command_list.index("-d")
                             + 1: command_list.index("-f")])
            create_file(command_list[command_list.index("-f")
                                     + 1:][0], directory_path)
        elif "-d" in command_list:
            create_dirs(command_list[command_list.index("-d") + 1:])
        elif "-f" in command_list:
            create_file(command_list[command_list.index("-f") + 1:][0])
    except Exception as exe:
        raise Exception(f"{exe}")


if __name__ == "__main__":
    main_run()
