import sys
import os
import datetime


def parse_input() -> dict:
    terminal_input = sys.argv[1:]
    to_do_dict = {"file": None, "directory": None}
    if ("-d" in terminal_input and "-f" in terminal_input
            and len(terminal_input) >= 4):
        file_index = terminal_input.index("-f")
        dir_index = terminal_input.index("-d")
        if file_index > dir_index:
            to_do_dict["directory"] = terminal_input[1:file_index]
            to_do_dict["file"] = terminal_input[file_index + 1]
            return to_do_dict

        to_do_dict["file"] = terminal_input[1:dir_index]
        to_do_dict["directory"] = terminal_input[dir_index + 1:]

    elif "-d" in terminal_input and len(terminal_input) > 2:
        dir_index = terminal_input.index("-d")
        to_do_dict["directory"] = terminal_input[dir_index:]

    elif "-f" in terminal_input and len(terminal_input) > 2:
        file_index = terminal_input.index("-f")
        to_do_dict["directory"] = terminal_input[file_index + 1]

    else:
        raise ValueError

    return to_do_dict


def create_directory(directory_path: str | list) -> str:
    if len(directory_path) == 1:
        destination_directory = os.path.join(os.getcwd(), directory_path)
    else:
        destination_directory = os.path.join(os.getcwd(), *directory_path)

    if os.path.exists(destination_directory):
        return destination_directory
    os.makedirs(destination_directory)
    return destination_directory


def add_content_to_file(file_name: str, directory_path: str) -> None:
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
    terminal_input = parse_input()
    file_name = "".join(terminal_input["file"])
    directory_path = create_directory(terminal_input["directory"])
    add_content_to_file(file_name=file_name, directory_path=directory_path)
