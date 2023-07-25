import sys
import os
from datetime import datetime


def get_directory_path(command: list[str]) -> str:
    return os.path.join(
        os.getcwd(),
        *command[command.index("-d") + 1:command.index("-f")]
        if "-f" in command
        else command[command.index("-d") + 1:]
    )


def create_file(command: list[str]) -> None:
    start_dir = os.getcwd()

    if "-d" in command:
        required_directory = get_directory_path(command)

        if not os.path.isdir(required_directory):
            os.makedirs(required_directory)

        os.chdir(required_directory)

    if "-f" in command:
        current_date = (
            ("\n\n" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            if os.path.isfile(
                os.path.join(
                    os.getcwd(),
                    command[command.index("-f") + 1]
                )
            )
            else str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

        with open(
                command[command.index("-f") + 1],
                "a"
        ) as created_modified_file:
            created_modified_file.write(current_date)

            line_to_write = input("Enter content line: ")
            line_number = 1
            while line_to_write != "stop":
                created_modified_file.write(
                    "\n" + str(line_number) + " " + line_to_write
                )
                line_to_write = input("Enter content line: ")
                line_number += 1

        os.chdir(start_dir)


create_file(sys.argv)
