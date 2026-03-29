def get_flags_indexes(commands_list: list) -> dict:
    try:
        directory_command_index = commands_list.index("-d")
    except ValueError:
        directory_command_index = -1

    try:
        file_command_index = commands_list.index("-f")
    except ValueError:
        file_command_index = -1

    if file_command_index < directory_command_index:
        raise ValueError("Unknown command")

    return {
        "dir": directory_command_index,
        "file": file_command_index,
    }


def get_directories_names(commands_list: list, directory_command_index: int,
                          file_command_index: int) -> str:
    directories_path = ""

    if directory_command_index > 0:
        if file_command_index > 0:
            path_parts = commands_list[(directory_command_index + 1):
                                       file_command_index]
        else:
            path_parts = commands_list[(directory_command_index + 1):]

        directories_path = "/".join(path_parts)

    return directories_path


def get_file_name_from_commands_list(commands_list: list,
                                     file_command_index: int) -> str:
    file_name = "file.txt"

    if file_command_index >= 0:
        file_name = commands_list[file_command_index + 1]

    return file_name
