import os
import sys
import datetime


def create_directory(directories: list) -> None:
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)


def parse_data(command_data: list) -> tuple:
    file_name = ""
    dir_path = []

    for value in command_data:
        if value.endswith(".txt"):
            file_name = value
            continue
        elif value in ["-f", "-d"]:
            continue
        dir_path.append(value)

    return file_name, dir_path


def create_file() -> None:
    command_data = sys.argv[1:]
    file_name, dir_path = parse_data(command_data)

    if dir_path:
        create_directory(dir_path)

    if file_name:
        file_name = os.path.join(*dir_path, file_name)

        with open(file_name, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content_to_write = f"{timestamp}\n"
            line_counter = 1
            while True:
                user_data = input("Enter content line (or 'stop' to finish):")
                if user_data == "stop":
                    content_to_write += "\n"
                    break
                content_to_write += f"{line_counter} {user_data}\n"
                line_counter += 1
            file.write(content_to_write)


if __name__ == "__main__":
    create_file()
