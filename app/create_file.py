import os
import sys
from functions import (
    validator,
    existing_file_content,
    content_to_file,
    dir_and_file_name_extraction,
)

command_to_execute = sys.argv[1:] if sys.argv else []
current_dir = os.getcwd()


def create_file() -> None:
    validation_result = validator(command_to_execute)

    if validation_result == 1:
        os.makedirs(
            os.path.join(current_dir, *command_to_execute[1:]),
            exist_ok=True,
        )

    elif validation_result == 2:
        file_name = command_to_execute[1]

        file_content = existing_file_content(file_name)

        content_to_file(file_content, file_name)

    elif validation_result == 3:
        command_data: dict = dir_and_file_name_extraction(
            command_to_execute
        )
        dirs, file_name = command_data.get("dirs"), command_data.get(
            "file_name"
        )
        file_path = os.path.join(*dirs, file_name)
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)

        file_content = existing_file_content(file_path)

        content_to_file(file_content, file_path)


create_file()
