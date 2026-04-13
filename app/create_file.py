import sys
import os
import datetime


def create_directories(term_entry: list) -> str:
    new_dirs = os.path.join("", *term_entry)
    os.makedirs(new_dirs, exist_ok=True)
    return new_dirs


def create_write_file(name: str) -> None:
    with open(name, "a") as file:
        file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        line = input("Enter content line: ")
        while line.lower() != "stop":
            file.write(f"{line}\n")
            line = input("Enter content line: ")
        file.write("\n")


def create_file_from_terminal() -> None:
    terminal_entry = sys.argv
    dir_entry_index = terminal_entry.index(
        "-d"
    ) if "-d" in terminal_entry else None
    file_entry_index = terminal_entry.index(
        "-f"
    ) if "-f" in terminal_entry else None
    file_name = terminal_entry[-1]

    if dir_entry_index is not None and file_entry_index is not None:
        path_entry = terminal_entry[dir_entry_index + 1:file_entry_index]
        file_name = f"{create_directories(path_entry)}/{file_name}"

    create_write_file(file_name)


if __name__ == "__main__":
    create_file_from_terminal()
