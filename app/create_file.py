import os
import sys
from datetime import datetime


def write_contents_to_file(filename: str) -> None:
    with open(filename, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1

        while (line_content := input("Enter content line: ")) != "stop":
            file.write(f"{line_number} {line_content}\n")
            line_number += 1

        file.write("\n")


def create_file() -> None:
    input_command = sys.argv

    if "-d" in input_command and "-f" in input_command:
        path = os.path.join(
            *input_command[input_command.index("-d")
                           + 1:input_command.index("-f")]
        )
        os.makedirs(path, exist_ok=True)
        write_contents_to_file(
            os.path.join(path, input_command[input_command.index("-f") + 1])
        )

    if "-f" not in input_command:
        path = os.path.join(
            *input_command[input_command.index("-d") + 1:]
        )
        os.makedirs(path, exist_ok=True)

    if "-d" not in input_command:
        write_contents_to_file(
            input_command[input_command.index("-f") + 1]
        )
