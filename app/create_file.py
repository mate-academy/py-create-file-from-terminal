from datetime import datetime
from os import makedirs, path
from sys import argv


def create_directory(dirs_list: list) -> str:
    dir_path = str(path.join(*dirs_list))
    makedirs(dir_path, exist_ok=True)
    return dir_path


def work_with_file(file_path: str) -> None:
    with open(file_path, "a+") as text_file:
        text_file.seek(0)
        if text_file.read():
            text_file.write("\n")
        text_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        count = 0
        while True:
            count += 1
            text = input("Enter content line: ")
            if text == "stop":
                break
            text_file.write(f"{count} {text}\n")


def work_with_console_input(console_input: list) -> None:
    if "-f" in console_input:
        if "-d" in console_input:
            dir_path = create_directory(console_input[1:-2])
            full_path = str(path.join(dir_path, console_input[-1]))
            work_with_file(full_path)
        else:
            work_with_file(console_input[-1])
    else:
        create_directory(console_input[1:])


work_with_console_input(argv[1:])
