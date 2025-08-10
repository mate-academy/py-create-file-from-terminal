import os
import sys
import datetime


def create_directory(new_directories: list) -> str:
    path_to_new_directory = os.path.join(*new_directories)
    if not os.path.exists(path_to_new_directory):
        os.makedirs(path_to_new_directory)
    return path_to_new_directory


def create_file(new_file_name: str) -> None:
    with open(new_file_name, "a") as new_file:
        current_date_time = datetime.datetime.now()
        timestamp = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(timestamp + "\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            new_file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:

    command = sys.argv[1:]

    if "-d" in command and "-f" in command:
        new_directories = command[command.index("-d") + 1: command.index("-f")]
        path_to_new_directory = create_directory(new_directories)
        path_to_new_file = \
            os.path.join(path_to_new_directory, f"{command[-1]}")
        create_file(path_to_new_file)

    elif "-d" in command:
        create_directory(command[command.index("-d") + 1:])

    elif "-f" in command:
        create_file(command[-1])


if __name__ == "__main__":
    main()
