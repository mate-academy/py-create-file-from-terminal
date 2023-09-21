import sys
import os
import datetime


def parse_input() -> tuple:
    terminal_input = sys.argv[1:]
    if "-d" in terminal_input and "-f" in terminal_input:
        file_index = terminal_input.index("-f")
        dir_index = terminal_input.index("-d")
        if file_index > dir_index:
            return ("".join(terminal_input[file_index + 1]),
                    terminal_input[dir_index + 1:file_index])
        else:
            return ("".join(terminal_input[file_index + 1]),
                    terminal_input[dir_index + 1:])

    elif "-d" in terminal_input:
        dir_index = terminal_input.index("-d")
        return None, terminal_input[dir_index + 1:],

    elif "-f" in terminal_input:
        file_index = terminal_input.index("-f")
        return "".join(terminal_input[file_index + 1]), None,

    else:
        raise ValueError


def create_directory(directory_path: list) -> str:
    if directory_path is None:
        return None
    destination_directory = os.path.join(os.getcwd(), *directory_path)
    os.makedirs(destination_directory, exist_ok=True)
    return destination_directory


def add_content_to_file(file_name: str,
                        directory_path: str | None = None) -> None:
    if file_name is None:
        return
    if directory_path is None:
        directory_path = os.getcwd()

    with open(os.path.join(directory_path, file_name), "a") as file:
        time_opened = (datetime.datetime.now()
                       .strftime("%Y-%m-%d %H:%M:%S") + "\n")
        file.write(time_opened)

        counter = 1
        content = input(f"Enter content line: Line{counter} ")
        while content != "stop":
            file.write(f"line{counter} " + content + "\n")
            content = input(f"Enter content line: Line{counter} ")
            counter += 1


if __name__ == "__main__":
    file_name, directory_path = parse_input()
    directory = create_directory(directory_path)
    add_content_to_file(file_name=file_name, directory_path=directory)
