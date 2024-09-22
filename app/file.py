from datetime import datetime
import os


def create_file(path: str) -> None:
    mode = "a" if os.path.exists(path) else "w"
    with open(path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        line_count = 1
        while True:
            content_line = str(input("Enter content line: "))
            if content_line.lower() == "stop":
                break
            file.write(f"{line_count} {content_line}\n")
            line_count += 1
