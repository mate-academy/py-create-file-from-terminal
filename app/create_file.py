import os
import sys
from datetime import datetime


# This function creating a file in a directory
def create_file(path: str, file_name: str | None) -> None:
    if file_name == "":
        return

    file_name = os.path.join(*[path, file_name])

    page_number = 1

    with open(file_name, "a") as file:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time_now}\n")
        while True:
            new_line_content = input("Enter content line: ")
            if new_line_content == "stop":
                file.write("\n")
                break
            file.write(f"{page_number} {new_line_content}\n")
            page_number += 1


# This function is creating a directory
def create_directory(path: str | None) -> None:
    if path == "":
        return
    os.makedirs(path, exist_ok=True)


# This function is parsing your command
def parse(command: list[str]) -> dict:
    file_name = ""
    path = ""

    if "-f" in command:
        file_name = command[-1]
        command.remove(file_name)
        command.remove("-f")

    if "-d" in command:
        d_index = command.index("-d")
        path = os.path.join(*command[d_index + 1:])

    return {
        "-f": file_name,
        "-d": path
    }


def main() -> None:

    arguments = sys.argv
    flags = parse(arguments)
    file_name = flags.get("-f")
    path = flags.get("-d")

    create_directory(path)
    create_file(path, file_name)


if __name__ == "__main__":
    main()
