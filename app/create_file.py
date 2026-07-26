import argparse
import datetime
import os


def create_path(directories: list[str]) -> str:
    return os.path.join(*directories)


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def add_timestamp() -> str:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return timestamp


def content_input(path: str) -> None:
    with open(path, "a") as file:
        file.write(f"{add_timestamp()}\n")
        line_counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{line_counter} {line}\n")
            line_counter += 1


def add_custom_commands(parser: argparse) -> None:
    args_list = [
        {
            "option": "-d",
            "dest": "directories",
            "type": str,
            "nargs": "*",
            "metavar": "directory",
            "help": "creates directories inside current directory",
        },
        {
            "option": "-f",
            "dest": "file_name",
            "type": str,
            "nargs": 1,
            "metavar": "filename",
            "help": "create file and input content lines until 'stop'",
        },
    ]

    for arg in args_list:
        parser.add_argument(
            arg["option"], dest=arg["dest"], type=arg["type"],
            nargs=arg["nargs"], metavar=arg["metavar"], help=arg["help"]
        )


if __name__ == "__main__":

    terminal_parser = argparse.ArgumentParser()
    add_custom_commands(terminal_parser)
    argument_in_terminal = terminal_parser.parse_args()
    current_working_directory = os.getcwd()

    if argument_in_terminal.directories:
        current_working_directory = create_path(
            argument_in_terminal.directories
        )
        create_directory(current_working_directory)

    if argument_in_terminal.file_name:
        path_to_file = [
            current_working_directory, argument_in_terminal.file_name[0]
        ]
        path = create_path(path_to_file)
        content_input(path)
