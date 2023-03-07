import os
import sys

from datetime import datetime


def create_file_from_command() -> None:
    command = sys.argv
    directory_path = ""
    file_name = ""

    if "-d" in command and "-f" not in command:
        directory_path = "/".join(command[1:])

    elif "-f" in command and "-d" not in command:
        file_name = command[1]

    elif "-d" and "-f" in command:
        index_of_f, index_of_d = command.index("-f"), command.index("-d")
        directory_path = "/".join(command[index_of_d:index_of_f])
        file_name = command[index_of_f + 1]

    full_dir_path = os.path.join(directory_path, file_name)
    os.makedirs(full_dir_path)

    with open("file_name", "a") as file:
        current_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
        file.write(current_date)
        line_count = 0

        while True:
            line_count += 1
            line_text = input("Enter content line: ")
            if line_text == "stop":
                break
            file.write(f"{line_count} {line_text}\n")


if __name__ == "__main__":
    create_file_from_command()
