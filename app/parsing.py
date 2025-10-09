def parse_path(command: list) -> tuple:
    directories, file_name = None, None
    if "-d" in command and "-f" in command:
        d_index = command.index("-d")
        f_index = command.index("-f")

        directories = (
            command[d_index + 1: f_index]
            if f_index > d_index
            else command[d_index + 1:]
        )
        file_name = command[f_index + 1]

    elif "-d" in command:
        directories = command[command.index("-d") + 1:]

    elif "-f" in command:
        file_name = command[command.index("-f") + 1]

    return directories or "", file_name or ""
