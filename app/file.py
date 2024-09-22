from datetime import datetime
import os


def create_file(path: str) -> None:
    mode = "a" if os.path.exists(path) else "w"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_write =f"{timestamp} + \n"
    line_count = 1
    while True:
        content_line = input("Enter content line: ")
        if content_line.lower() == "stop":
            break
        file_write += f"{line_count} {content_line}\n"
        line_count += 1
    with open(path, mode) as file:
        file.write(file_write)
        