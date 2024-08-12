import datetime
import os
import sys


def create_dir(directories: list) -> None:
    path_to_file = os.path.join(*directories)
    os.makedirs(path_to_file, exist_ok=True)


def create_new_file(new_file: str) -> None:
    with open(new_file, "a") as result_file:
        creation_time = datetime.datetime.now()
        counter = 1
        result_file.write(f"{creation_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            new_text_line = input("enter additional "
                                  "text line or enter 'stop' to stop:_ ")
            if new_text_line != "stop":
                result_file.write(f"{counter} {new_text_line}\n")
                counter += 1
            else:
                result_file.write("\n")
                break


def create_file() -> None:
    command = sys.argv

    d_index = command.index("-d") if "-d" in command else None
    f_index = command.index("-f") if "-f" in command else None

    dirs = command[d_index + 1: f_index] if d_index is not None else []
    new_file = os.path.join(*dirs, command[-1]) if "-f" in command else None

    if dirs:
        create_dir(dirs)

    if new_file:
        create_new_file(new_file)


if __name__ == "__main__":
    create_file()
