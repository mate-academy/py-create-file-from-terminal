import os
import sys
import datetime


def enter_content(opening_mode: str) -> str:
    file_content = ""
    line_content = ""
    count = 1
    while line_content != "stop":
        line_content = input("Enter content line: ")
        if line_content != "stop":
            if opening_mode == "w":
                file_content += f"{count} Line{count} {line_content}\n"
            else:
                file_content += f"{count} Another line{count} {line_content}\n"
            count += 1
    return file_content + "\n"


def create_directory(folders: list) -> str:
    path = os.path.join("app")
    for folder in folders[folders.index("-d") + 1:]:
        if folder == "-f":
            break
        path += os.path.join("/", folder)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: list) -> None:
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "-d" not in file_name:
        path = os.path.join("app/", file_name[-1])
    else:
        path = os.path.join(
            create_directory(file_name), file_name[file_name.index("-f") + 1]
        )
    if not os.path.exists(path):
        opening_mode = "w"
    else:
        opening_mode = "a"
    with open(path, opening_mode) as new_file:
        file_content = f"{date_time}\n" + enter_content(opening_mode)
        new_file.write(file_content)


def main(directory: list) -> create_directory:
    if "-d" in directory and "-f" not in directory:
        create_directory(directory)
    else:
        create_file(directory)


main(sys.argv[1:])
