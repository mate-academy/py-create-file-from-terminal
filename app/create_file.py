from datetime import datetime
import os
import sys


def create_file_from_terminal() -> None:
    commands = sys.argv
    if "-f" in commands:
        index_f = commands.index("-f")
        file_name = commands[index_f + 1:]

        if "-d" in commands:
            index_d = commands.index("-d")
            name_dir = commands[index_d + 1:index_f]
            dir_path = os.path.join(*name_dir)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            full_path = os.path.join(dir_path, file_name[0])
        else:
            full_path = file_name[0]

        write_content(full_path)

    elif "-f" not in commands and "-d" in commands:
        index_d = commands.index("-d")
        name_dir = commands[index_d + 1:]
        dir_path = os.path.join(*name_dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


def write_content(full_path) -> None:
    line_number = 1
    file_content = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    while True:
        line_content = input("Enter content line: ")
        if line_content == "stop":
            break
        file_content += f"{line_number} Line{line_number} {line_content}\n"
        line_number += 1

    with open(full_path, "a") as f:
        f.write(file_content)
        f.write("\n")


if __name__ == "__main__":
    create_file_from_terminal()
