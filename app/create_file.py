import os
import sys
import datetime


def create_file_from_terminal() -> None:

    command_string = sys.argv[1:]
    directory_path: str | None = None
    file_name: str | None = None
    dir_path_parts: list[str] = []

    if "-d" in command_string:
        d_index = command_string.index("-d")
        for part in command_string[d_index + 1:]:
            if part.startswith("-"):
                break
            dir_path_parts.append(part)
        directory_path = os.sep.join(dir_path_parts)

    if "-f" in command_string:
        f_index = command_string.index("-f")
        file_name = command_string[f_index + 1]

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        if directory_path:
            full_file_path = os.path.join(directory_path, file_name)
        else:
            full_file_path = file_name

        page_number = 1
        with open(full_file_path, "a") as file:
            current_date = datetime.datetime.now()
            file.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    file.write("\n")
                    break
                file.write(f"{page_number}. {text}\n")
                page_number += 1


create_file_from_terminal()
