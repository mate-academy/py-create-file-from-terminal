import sys
import os
from datetime import datetime


def get_command_flags() -> dict:
    command = sys.argv[1:]
    flag_items = {}

    for i in range(len(command)):
        f = None
        d = None
        if command[i] == "-f":
            flag_items["-f"] = command[i + 1]
            f = i
        elif command[i] == "-d":
            d = i








def create_path(
        directories: list[str],
        file_name: str
) -> str:
    path = ""

    if directories != []:
        path = os.path.join(*directories)
        if not os.path.exists(path):
            os.makedirs(path)

    return os.path.join(path, file_name)


def create_file():
    flag_values = get_command_flags()
    path = create_path(flag_values["-d"], flag_values["-f"])

    with open(path, "a") as file:
        file.write(datetime.now().isoformat())
        line_pointer = 1
        while True:
            content = input("Enter content line: ")

            if content == "stop":
                break

            file.write(f"{line_pointer} {content}")
            line_pointer += 1


if __name__ == "__main__":
    create_file()
