import os
import sys
from functions import (
    validator,
    fill_the_file,
    dir_and_file_name_extraction,
)

command_to_execute = sys.argv[1:] if sys.argv else []
current_dir = os.getcwd()
print(command_to_execute)


def create_file() -> None:
    if validator(command_to_execute) == 1:
        os.makedirs(
            os.path.join(current_dir, *command_to_execute[1:])
        )

    elif validator(command_to_execute) == 2:
        file_name = command_to_execute[1]
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                file_content = f.read()
        else:
            file_content = ""

        if len(file_content) == 0:
            with open(file_name, "a") as f:
                info_to_write = fill_the_file().rstrip("\n")
                f.write(info_to_write)
        else:
            with open(file_name, "a") as f:
                info_to_write = "\n" * 2 + fill_the_file().rstrip(
                    "\n"
                )
                f.write(info_to_write)

    elif validator(command_to_execute) == 3:
        command_data: dict = dir_and_file_name_extraction(
            command_to_execute
        )
        dirs, file_name = command_data.get("dirs"), command_data.get(
            "file_name"
        )
        file_path = os.path.join(*dirs, file_name)

        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
            with open(file_path, "w"):
                pass

        with open(file_path, "r") as f:
            file_content = f.read()

        if len(file_content) == 0:
            with open(file_path, "a") as f:
                info_to_write = fill_the_file().rstrip("\n")
                f.write(info_to_write)
        else:
            with open(file_path, "a") as f:
                info_to_write = "\n" * 2 + fill_the_file().rstrip(
                    "\n"
                )
                f.write(info_to_write)


create_file()
