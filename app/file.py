import os
from datetime import datetime


def file_spawn(file_path: str) -> None:
    mode = "a" if os.path.exists(file_path) else "w"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_write = f"{timestamp}\n"
    line_num = 1
    while True:
        input_line = input("Enter content line:")
        if input_line.lower() == "stop":
            file_write += "\n"
            break
        file_write += f"{line_num} {input_line}\n"
        line_num += 1

    with open(file_path, mode) as file:
        file.write(file_write)
