import sys
import os
from datetime import datetime


def make_dir(path: list) -> str:
    path = os.path.join(*path)
    os.makedirs(path, exist_ok=True)
    return path


def creating_the_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date_time}\n")
        while True:
            line = input("Enter content line: ")
            counter = 1
            if line != "stop":
                file.write(f"{counter} {line}\n")
                counter += 1
                continue
            break


def main() -> None:
    cmd_line = sys.argv
    if "-d" in cmd_line and "-f" in cmd_line:
        new_path = make_dir(
            cmd_line[cmd_line.index("-d") + 1:cmd_line.index("-f")]
        )
        os.chdir(new_path)
        creating_the_file(cmd_line[cmd_line.index("-f") + 1])

    elif "-f" in cmd_line and "-d" not in cmd_line:
        creating_the_file(cmd_line[cmd_line.index("-f") + 1])

    elif "-d" in cmd_line and "-f" not in cmd_line:
        make_dir(cmd_line[cmd_line.index("-d") + 1:])


if __name__ == "__main__":
    main()
