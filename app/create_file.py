import os
import sys
from parse_commands.parse_commands import (get_flags_indexes,
                                           get_directories_names,
                                           get_file_name_from_commands_list)
from get_data.get_data import get_file_content_from_user
from fill_file.fill_file import write_data_to_file


def create_file() -> None:
    commands_list = sys.argv

    flags = get_flags_indexes(commands_list)

    directory_command_index = flags["dir"]
    file_command_index = flags["file"]

    directories = get_directories_names(commands_list, directory_command_index,
                                        file_command_index)

    file_name = get_file_name_from_commands_list(commands_list,
                                                 file_command_index)

    file_path = file_name

    if directories:
        os.makedirs(directories)
        file_path = directories + "/" + file_name

    with open(file_path, "w"):
        pass

    lines = get_file_content_from_user()

    write_data_to_file(file_path, lines)


create_file()
