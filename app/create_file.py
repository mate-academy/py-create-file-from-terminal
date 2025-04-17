import os
from datetime import datetime


def create_directory(path_parts: list[str]) -> None:
    path = os.path.join(*path_parts)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
        return path
    except OSError as e:
        print(f"Error creating directory {path}: {e}")
        return None


def create_or_append_file(file_path: str) -> bool:
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lines = []
        print("Enter content lines (type stop to finish):")
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            lines.append(line)

        content_to_write = [timestamp] + [f"{i + 1} {line}"
                                          for i, line in enumerate(lines)]

        if os.path.exists(file_path):
            with open(file_path, "a") as f:
                f.write("\n")
                f.write("\n".join(content_to_write))
            print(f"Content appended to file: {file_path}")
        else:
            with open(file_path, "w") as f:
                f.write("\n".join(content_to_write))
            print(f"File created: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating/appending to file {file_path}: {e}")
        return False
