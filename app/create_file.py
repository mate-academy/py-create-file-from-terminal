import sys
import os
import datetime


def create_directories(term_entry: list) -> str:
    term_entry.remove("-f")
    new_dirs_str = "/".join(term_entry)
    new_dirs = os.path.dirname(new_dirs_str)
    os.makedirs(new_dirs)
    return new_dirs_str


def create_write_file(name: str) -> None:
    with open(name, "a") as file:
        file.write(
            f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
        )
        line = input("Enter content line: ")
        while line.lower() != "stop":
            file.write(f"{line}\n")
            line = input("Enter content line: ")


def create_file_from_terminal() -> None:
    terminal_entry = sys.argv
    dir_entry_index = terminal_entry.index(
        "-d"
    ) if "-d" in terminal_entry else False
    file_name = terminal_entry[-1]

    if dir_entry_index:
        path_entry = terminal_entry[dir_entry_index + 1:]
        file_name = create_directories(path_entry)

    create_write_file(file_name)


if __name__ == "__main__":
    create_file_from_terminal()
